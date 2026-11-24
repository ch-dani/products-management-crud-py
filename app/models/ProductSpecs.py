from app.db.base import Base
from datetime import datetime
from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column

class ProductSpecs(Base):
    __tablename__ =  "product_specs"
    id : Mapped[int] = mapped_column(primary_key=True)
    ps_key : Mapped[str] = mapped_column(String(100))
    ps_value : Mapped[str] = mapped_column(String(100))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now())
