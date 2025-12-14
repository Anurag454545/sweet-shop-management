from fastapi import APIRouter, Depends, Query, HTTPException
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


@router.get("")
def list_sweets(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Sweet).all()


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


@router.put("/{sweet_id}")
def update_sweet(
    sweet_id: int,
    sweet: schemas.SweetCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_sweet = db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()

    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db_sweet.name = sweet.name
    db_sweet.price = sweet.price
    db_sweet.quantity = sweet.quantity

    db.commit()
    db.refresh(db_sweet)

    return db_sweet
