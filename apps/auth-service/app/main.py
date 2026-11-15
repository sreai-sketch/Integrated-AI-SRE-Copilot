import os
import sqlite3
from contextlib import closing
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pwdlib import PasswordHash

DB = Path(os.getenv("AUTH_DB", "/data/auth.db"))
SECRET = os.getenv("JWT_SECRET", "local-only-change-this-secret-before-sharing")
PASSWORD_HASH = PasswordHash.recommended()
app = FastAPI(title="Survey Auth Service", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8081"], allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["Authorization", "Content-Type"])

class Credentials(BaseModel):
    email: EmailStr
    password: str


def connect():
    DB.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB)


def init_db():
    with closing(connect()) as con:
        con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)")
        con.commit()
        demo_email = os.getenv("DEMO_EMAIL", "demo@example.com").lower()
        demo_password = os.getenv("DEMO_PASSWORD", "ChangeMe123!")
        existing = con.execute("SELECT id FROM users WHERE email=?", (demo_email,)).fetchone()
        if not existing:
            con.execute("INSERT INTO users(email,password_hash) VALUES (?,?)", (demo_email, PASSWORD_HASH.hash(demo_password)))
            con.commit()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "service": "auth-service"}

@app.post("/register", status_code=201)
def register(body: Credentials):
    if len(body.password) < 10:
        raise HTTPException(400, "Password must contain at least 10 characters")
    try:
        with closing(connect()) as con:
            cur = con.execute("INSERT INTO users(email,password_hash) VALUES (?,?)", (body.email.lower(), PASSWORD_HASH.hash(body.password)))
            con.commit()
            user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(409, "Email is already registered")
    return {"user_id": user_id, "email": body.email.lower()}

@app.post("/login")
def login(body: Credentials):
    with closing(connect()) as con:
        row = con.execute("SELECT id,password_hash FROM users WHERE email=?", (body.email.lower(),)).fetchone()
    if not row or not PASSWORD_HASH.verify(body.password, row[1]):
        raise HTTPException(401, "Invalid email or password")
    now = datetime.now(timezone.utc)
    token = jwt.encode({"sub": str(row[0]), "email": body.email.lower(), "iat": now, "exp": now + timedelta(hours=2)}, SECRET, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer", "expires_in": 7200}
