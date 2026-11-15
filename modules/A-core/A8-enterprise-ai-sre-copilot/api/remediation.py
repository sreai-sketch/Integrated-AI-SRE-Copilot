from fastapi import APIRouter
router=APIRouter()
@router.get("/remediation/safety")
def safety(): return {"automatic_execution":False,"human_approval_required":True}
