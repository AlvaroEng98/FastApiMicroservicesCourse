from fastapi import APIRouter

from apps.models.product import Product

router = APIRouter(prefix="/products",tags=["product"])


@router.get("/all")
def get_all_products():
    return Product.all_pks()

