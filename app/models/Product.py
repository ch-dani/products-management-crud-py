from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func

class Product(Base):
    __tablename__ = "products"
    id : Mapped[int] = mapped_column(primary_key=True)
    category_id : Mapped[int | None] = mapped_column(default=None)
    title : Mapped[str] = mapped_column(String(100))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(onupdate=func.now(), default=None)
 