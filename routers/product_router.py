from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.schemas.response_wrapper import APIResponse


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

from app.controllers.admin_controllers import product_controller

@router.get("/")
def get_products():
    return product_controller.get_products()

@router.post("/", response_model=APIResponse[ProductResponse])
def create_product(data: ProductCreate):
    return product_controller.create_product(data)

@router.post("/{id}/update")
def update_product():
    return product_controller.update_product()

@router.delete("/{id}")
def delete_product():
    return product_controller.delete_product()
