from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password_hash: str = Field(min_length= 6, max_length=30)
    first_name: str 
    last_name: str
    
class UserModel(BaseModel):
    uid:uuid.UUID 
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool= Field(default=False)
    password_hash: str = Field(exclude=True)
    created_at: datetime 
    updated_at: datetime 


class UserLoginModel(BaseModel):
    email: str
    password: str = Field(exclude=True)