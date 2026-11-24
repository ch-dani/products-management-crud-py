from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

T= TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success : bool =  True
    message : str = "Request successfully"
    data : Optional[T] = None

    # def __init__(self, **kwargs):
    #     if "data" in kwargs and kwargs["data"] is not None:
    #         kwargs["data"] = jsonable_encoder(kwargs["data"])
    #     super().__init__(**kwargs)