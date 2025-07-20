from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from bson import ObjectId
from database import products_collection, orders_collection
from models import *
from pymongo import DESCENDING
import uvicorn

app = FastAPI()

@app.post("/products", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    doc = product.dict()
    result = await products_collection.insert_one(doc)
    return {"id": str(result.inserted_id)}

@app.get("/products", response_model=ProductListResponse)
async def list_products(name: Optional[str] = None, size: Optional[str] = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = await products_collection.find(query).skip(offset).limit(limit)
    data = []
    for p in cursor:
        data.append({"id": str(p["_id"]), "name": p["name"], "price": p["price"]})

    return {
        "data": data,
        "page": {
            "limit": limit,
            "next": offset + limit,
            "previous": max(offset - limit, 0)
        }
    }

@app.post("/orders", response_model=ProductResponse, status_code=201)
async def create_order(order: OrderCreate):
    result = await orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@app.get("/orders/{user_id}", response_model=OrderListResponse)
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = await orders_collection.find({"userId": user_id}).skip(offset).limit(limit)
    data = []
    for order in cursor:
        total = 0
        items = []
        for item in order["items"]:
            product = products_collection.find_one({"_id": ObjectId(item["productId"])})
            name = product["name"] if product else "Unknown"
            price = product["price"] if product else 0
            total += price * item["qty"]
            items.append({
                "productDetails": {
                    "name": name,
                    "id": item["productId"]
                },
                "qty": item["qty"]
            })
        data.append({
            "id": str(order["_id"]),
            "items": items,
            "total": total
        })

    return {
        "data": data,
        "page": {
            "limit": limit,
            "next": offset + limit,
            "previous": max(offset - limit, 0)
        }
    }

@app.get("/")
def root():
    return {"message": "API working!"}
