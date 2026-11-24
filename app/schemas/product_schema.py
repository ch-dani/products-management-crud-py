from pydantic import BaseModel,ConfigDict
from datetime import datetime
from pydantic.alias_generators import to_camel

class ProductCreate(BaseModel):
    category_id: int
    title: str
    


class ProductResponse(BaseModel):
    id: int
    category_id: int
    title: str
    created_at : datetime
    model_config = ConfigDict(
        from_attributes=True, 
        alias_generator=to_camel,
        populate_by_name=True
    )
