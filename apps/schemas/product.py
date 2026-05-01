from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    pk: str
    name: str
    price: float
    quantity: int

    model_config = {"from_attributes": True}
