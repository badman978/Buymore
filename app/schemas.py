from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class Users(BaseModel):
    username: str
    password: str
    email: EmailStr 
    phone_no: str

# class ProductCategoryBase(BaseModel):
#     category_name: str

# class ProductCategoryCreate(ProductCategoryBase):
#     pass

# class ProductCategory(ProductCategoryBase):
#     id: int

#     class Config:
#         orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    qty_in_stock: int
    price: str
    product_image: Optional[str] = None

class UserCart(BaseModel):
    name: str
    description: str
    qty_in_stock: int
    price: str
    product_image: Optional[str] = None

class CartCreate(BaseModel):
    user_id: int
# class ProductCreate(ProductBase):
#     category: ProductCategoryCreate

# class Product(ProductBase):
#     id: int
#     category: ProductCategory

#     class Config:
#         orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str

class Country(BaseModel):
    country: str

class UserAddress(BaseModel):   
    unit_number : str
    street_number : str
    address_line_1: str
    address_line_2: str
    city : str
    region : str
    postal_code : str