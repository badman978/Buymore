from typing import List
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

from ..database import get_db
from .. import models, responses, schemas, utils, oauth2
#


router = APIRouter(
    prefix="/usercart",
    tags=['User Cart']
)


#use the product id to query the database and then send necessary data to user cart database

#create user cart db
@router.post('/{id}', status_code=status.HTTP_201_CREATED, response_model=responses.Carts)
def add_item_to_cart(id:int, user_cart: schemas.UserCart, db: Session = Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.ShoppingCart).filter(models.ShoppingCart.user_id == id).first()
    if query == None:
        raise HTTPException(status.HTTP_204_NO_CONTENT, detail="User cart does not exist")
    if query.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User not authorized to perform action")
    new_item = models.ShoppingCartItem(**user_cart.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

#not really an important route 
@router.get('/{id}', response_model=List[responses.Carts])
def get_user_cart(id: int, db: Session = Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.ShoppingCartItem).filter(models.ShoppingCart.user_id == user.id)
    cart = query.first()

    if query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id({id}) does not exist")

    if cart.id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized to perfrom requested action")
    return cart

#get products from user cart
@router.get('/{id}/carts', response_model= List[responses.Carts])
def get_cart_item(id: int, db: Session = Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    if user.id != id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authorized to perform action")

    if id == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"No user with id of {id} has a cart. First create one.")
    
    
    query = db.query(models.ShoppingCartItem).filter(models.ShoppingCartItem.cart_id == id)
    return query
    pass



#add products to user cart
@router.post('/{id}/{product_id}', response_model= responses.Carts)
def add_cart_item(id: int, product_id:int, db: Session = Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    if user.id != id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authorized to perform action")
    query = db.query(models.ShoppingCart).filter(models.ShoppingCart.user_id == id)
    if query == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"No user with a user_cart id of {id}. First create one.")
    if user.id != query.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details="not authorized to perform action")
    product_query = db.query(models.Products).filter(models.Products.id == product_id).first()
    if product_query.id != product_id:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, details= f"product with id:{product_id}, was not found")
    
        
    add_to_cart = models.ShoppingCartItem(**product_id.dict())
    db.add(add_to_cart)
    db.commit()
    db.refresh(add_to_cart)

    return status.HTTP_202_ACCEPTED

    pass