from typing import List

from fastapi import APIRouter, status
from apps.models.product import Product
from apps.schemas.product import ProductResponse, ProductCreate

router = APIRouter(prefix="/products",tags=["product"])


@router.get("/all", response_model=List[ProductResponse])
def get_all_products():
    pks = list(Product.all_pks())
    return [Product.get(pk) for pk in pks]


@router.post("/add"  , response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate):
    product = Product(**data.model_dump())
    product.save()
    return product

@router.get("/{pk}", response_model=ProductResponse)
def get_product_by_id(pk: str):
    product = Product.get(pk)
    return product

@router.delete("/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)
