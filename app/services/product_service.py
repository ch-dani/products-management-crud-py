
from sqlalchemy.orm import Session
from app.models.Product import Product
from app.schemas.product_schema import ProductCreate
from app.db.database import get_db
from app.schemas.response_wrapper import APIResponse

def create_product(data: ProductCreate):
    db = next(get_db())
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)

    return APIResponse(data=product, success=True, message="Product created successfully")
    
    
