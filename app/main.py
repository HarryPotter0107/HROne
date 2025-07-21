from fastapi import FastAPI
from app.routes import product, order

app = FastAPI(title="HROne API")

@app.get("/")
def read_root():
    return {"message": "Welcome to HROne API!"}

# Register API routers
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
