from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Product model
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

# Fake database
products = []

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added", "product": product}
