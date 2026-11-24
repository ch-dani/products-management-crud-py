from app.controllers.admin_controllers import product_category_controller
from fastapi import APIRouter
router = APIRouter(
    prefix="/product_categories",
    tags=["product_categories"]
)

@router.get("/")
def product_categories():
    return product_category_controller.get_product_categories()


@router.post("/")
def create_product_category():
    return product_category_controller.create_product_category()


@router.post("/{id}/update")
def update_product_category(id: int):
    return product_category_controller.update_product_category()

@router.delete("/{id}")
def delete_product_category(id: int):
    return product_category_controller.delete_product_category()

