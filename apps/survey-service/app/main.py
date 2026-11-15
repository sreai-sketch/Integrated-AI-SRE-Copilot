import os
import sqlite3
from contextlib import closing
from pathlib import Path

import jwt
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

DB = Path(os.getenv("SURVEY_DB", "/data/survey.db"))
SECRET = os.getenv("JWT_SECRET", "local-only-change-this-secret-before-sharing")
app = FastAPI(title="Survey Results Service", version="0.1.0")

class Submission(BaseModel):
    question_id: str = Field(min_length=1, max_length=80)
    question: str = Field(min_length=3, max_length=300)
    answer: str = Field(min_length=1, max_length=500)


def connect():
    DB.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB)

@app.on_event("startup")
def startup():
    with closing(connect()) as con:
        con.execute("CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY, user_id TEXT NOT NULL, question_id TEXT NOT NULL, question TEXT NOT NULL, answer TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
        con.commit()

def current_user(authorization: str | None):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "Login required")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["sub"]
    except (jwt.InvalidTokenError, KeyError):
        raise HTTPException(401, "Invalid or expired login token")

@app.get("/health")
def health():
    return {"status": "ok", "service": "survey-service"}

@app.get("/", response_class=HTMLResponse)
def page():
    return HTMLResponse(PAGE)

@app.post("/submissions", status_code=201)
def submit(body: Submission, authorization: str | None = Header(default=None)):
    user_id = current_user(authorization)
    with closing(connect()) as con:
        cur = con.execute("INSERT INTO submissions(user_id,question_id,question,answer) VALUES (?,?,?,?)", (user_id, body.question_id, body.question, body.answer))
        con.commit()
        return {"submission_id": cur.lastrowid, "status": "recorded"}

@app.get("/results")
def results(question_id: str = "daily-pulse"):
    with closing(connect()) as con:
        rows = con.execute("SELECT answer, COUNT(*) FROM submissions WHERE question_id=? GROUP BY answer ORDER BY COUNT(*) DESC", (question_id,)).fetchall()
        total = con.execute("SELECT COUNT(*) FROM submissions WHERE question_id=?", (question_id,)).fetchone()[0]
    return {"question_id": question_id, "total_responses": total, "results": [{"answer": answer, "count": count, "percentage": round(count * 100 / total, 1) if total else 0} for answer, count in rows]}

PAGE = r'''<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Daily Pulse Survey</title>
<style>body{font:16px system-ui;max-width:760px;margin:40px auto;padding:0 18px;color:#18212f}section{border:1px solid #ddd;border-radius:12px;padding:18px;margin:16px 0}input,button,select{padding:10px;margin:5px;border:1px solid #bbb;border-radius:7px}button{cursor:pointer}li{margin:8px 0}.muted{color:#666}</style></head>
<body><h1>Daily Pulse Survey</h1><p class="muted">A tiny two-microservice demo: authenticate, submit a response, and view everyone’s combined results.</p>
<section><h2>1. Login</h2><input id="email" value="demo@example.com" aria-label="Email"><input id="password" type="password" value="ChangeMe123!" aria-label="Password"><button onclick="login()">Login</button><p id="loginStatus" class="muted">Not logged in</p></section>
<section><h2>2. Random survey question</h2><p id="question"></p><select id="answer"><option>Very good</option><option>Good</option><option>Average</option><option>Needs improvement</option></select><button onclick="submitAnswer()">Submit answer</button><p id="submitStatus"></p><button onclick="newQuestion()">Pick another question</button></section>
<section><h2>3. Combined results (all participants)</h2><button onclick="loadResults()">Refresh results</button><p id="total"></p><ul id="results"></ul></section>
<script>
const questions=[{id:'daily-pulse',q:'How would you rate your day so far?'},{id:'team-health',q:'How clear are your current priorities?'},{id:'service-health',q:'How satisfied are you with the service experience?'}];let selected=questions[0],token='';
function newQuestion(){selected=questions[Math.floor(Math.random()*questions.length)];document.getElementById('question').textContent=selected.q;}
async function login(){const r=await fetch('http://localhost:8080/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:document.getElementById('email').value,password:document.getElementById('password').value})});const d=await r.json();if(!r.ok){document.getElementById('loginStatus').textContent=d.detail||'Login failed';return;}token=d.access_token;document.getElementById('loginStatus').textContent='Logged in successfully.';}
async function submitAnswer(){if(!token){document.getElementById('submitStatus').textContent='Please login first.';return;}const r=await fetch('/submissions',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+token},body:JSON.stringify({question_id:selected.id,question:selected.q,answer:answer.value})});const d=await r.json();document.getElementById('submitStatus').textContent=r.ok?'Response recorded.':(d.detail||'Submission failed');if(r.ok)loadResults();}
async function loadResults(){const r=await fetch('/results?question_id='+encodeURIComponent(selected.id));const d=await r.json();document.getElementById('total').textContent='Total responses: '+d.total_responses;const list=document.getElementById('results');list.innerHTML='';d.results.forEach(x=>{const li=document.createElement('li');li.textContent=x.answer+': '+x.count+' ('+x.percentage+'%)';list.appendChild(li);});}
newQuestion();loadResults();
</script></body></html>'''
