from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.deps import get_current_user
from app import models, schemas

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_sweets(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(models.Sweet).all()


@router.post("/")
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
