from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from app import schemas

class Users(BaseModel):
    username: str
    email: EmailStr
    phone_no: str
    id: int

    class Config:
        orm_mode = True

class ProductCategoryResponse(BaseModel):
    category: schemas.ProductBase

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    qty_in_stock: int
    price: str
    product_image: Optional[str] = None
    created_at: datetime
    class Config:
        orm_mode = True

class Carts(BaseModel):
    name: str
    description: str
    qty_in_stock: int
    price: str
    product_item_id: int
    product_image: Optional[str] = None
    added_at: datetime
    class Config:
        orm_mode = True


class Country(BaseModel):
    country: str
    
    class Config:
        orm_mode = True
    
class Address(BaseModel):
    country: str
    city: str
    address_line_1: str
    street_number: str
    unit_number: str

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True