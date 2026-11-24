from app.db.base import Base
from sqlalchemy import String,func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class ProductCategory(Base):
    __tablename__ = "product_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id : Mapped[int | None] = mapped_column(default=None)
    title : Mapped[str] = mapped_column(String(500))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(onupdate=func.now(),default=None)
