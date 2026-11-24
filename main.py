from routers import product_router
from routers import product_category_router
from fastapi import FastAPI
app = FastAPI()

app.include_router(product_router.router)
app.include_router(product_category_router.router)

# @app.get("/")
# def home(): 
#     return {"detail" : "hello home"}

   