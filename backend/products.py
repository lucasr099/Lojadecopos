from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import Product
from schemas import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse)
def add_product(data: ProductCreate, db: Session = Depends(get_db)):
    new = Product(**data.model_dump())  # pydantic -> dict
    db.add(new)
    db.commit()
    db.refresh(new)
    return new
