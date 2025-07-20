from pydantic import BaseModel
from typing import List, Optional

class ProductSize(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[ProductSize]

class ProductResponse(BaseModel):
    id: str

class ProductItem(BaseModel):
    id: str
    name: str
    price: float

class ProductListResponse(BaseModel):
    data: List[ProductItem]
    page: dict

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderProductDetails(BaseModel):
    name: str
    id: str

class OrderItemResponse(BaseModel):
    productDetails: OrderProductDetails
    qty: int

class OrderResponse(BaseModel):
    id: str
    items: List[OrderItemResponse]
    total: float

class OrderListResponse(BaseModel):
    data: List[OrderResponse]
    page: dict
