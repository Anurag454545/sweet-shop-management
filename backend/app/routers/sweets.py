from fastapi import APIRouter

router = APIRouter(prefix="/api/sweets")

@router.get("")
def list_sweets():
    return []

@router.post("")
def add_sweet():
    return {"message": "Sweet added"}
