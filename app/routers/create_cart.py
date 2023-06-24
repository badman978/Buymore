from typing import List
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

from ..database import get_db
from .. import models, responses, schemas, utils, oauth2
#


router = APIRouter(
    prefix="/createcart",
    tags=['Create User Cart']
)


@router.post('/{id}', status_code=status.HTTP_201_CREATED)
def create_user_cart(id:int, user_cart: schemas.CartCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # query = db.query(models.Users).filter(models.Users.id == id)
    # cart = query.first()
    # if query.first() == None:
    #     raise HTTPException(status.HTTP_204_NO_CONTENT, detail=f"User with id{id} does not exist")
    # if cart.id != user_id.id:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    #                         detail="Not authorized to perfrom requested action")
    new_cart = models.ShoppingCart(**user_cart.dict())
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    return status.HTTP_201_CREATED

