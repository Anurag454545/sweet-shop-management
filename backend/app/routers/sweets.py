from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.deps import get_current_user
from app import models, schemas

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)


# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- LIST SWEETS (PROTECTED) ----------------
@router.get("")
def list_sweets(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Sweet).all()


# ---------------- ADD SWEET (PROTECTED) ----------------
@router.post("")
def add_sweet(
    sweet: schemas.SweetCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_sweet = models.Sweet(
        name=sweet.name,
        price=sweet.price,
        quantity=sweet.quantity
    )

    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)

    return new_sweet


# ---------------- SEARCH SWEETS (PROTECTED) ----------------
@router.get("/search")
def search_sweets(
    query: str = Query(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return (
        db.query(models.Sweet)
        .filter(models.Sweet.name.ilike(f"%{query}%"))
        .all()
    )
