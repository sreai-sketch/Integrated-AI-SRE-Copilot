from fastapi import APIRouter
from models import ApprovalRequest
from approval_manager import decide
router=APIRouter()
@router.post("/approvals")
def submit(request:ApprovalRequest): return decide(request.decision)
