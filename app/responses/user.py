from typing import Union
from datetime import datetime
from app.responses.base import BaseResponse
from pydantic import EmailStr

class UserResponse(BaseResponse):
    id:int
    name:str
    email:EmailStr
    is_active:bool
    created_at:Union[str, None, datetime] = None