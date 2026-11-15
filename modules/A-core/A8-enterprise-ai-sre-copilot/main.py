from fastapi import FastAPI
from api.incidents import router as incidents
from api.approvals import router as approvals
from api.remediation import router as remediation
app=FastAPI(title="AI SRE Copilot Starter")
app.include_router(incidents); app.include_router(approvals); app.include_router(remediation)
@app.get("/health")
def health(): return {"status":"healthy"}
