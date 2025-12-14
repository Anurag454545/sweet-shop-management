from fastapi import APIRouter, Depends
from app.deps import get_current_user

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)


@router.get("/")
def list_sweets(current_user=Depends(get_current_user)):
    return []
