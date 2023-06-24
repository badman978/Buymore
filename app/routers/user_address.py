from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

from ..database import  get_db
from .. import models, responses, schemas, utils, oauth2
#


router = APIRouter(
    prefix= "/address",
    tags=['User Address']
)


@router.post("/", response_model=responses.Country)
def create_product(country: schemas.Country ,db: Session =Depends(get_db)):
    user_country = models.Country(**country.dict())
    db.add(user_country)
    db.commit()
    db.refresh(user_country)

    return user_country

@router.post("/", response_model=responses.Address)
def create_product(address: schemas.UserAddress ,db: Session =Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    user_address = models.Address(**address.dict())
    #add data to the UserAddress table
    db.add(user_address)
    db.commit()
    db.refresh(user_address)

    return user_address

@router.get('/{id}', response_model=List[responses.Address])
def get_user_cart(id: int, db: Session = Depends(get_db), user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.UserAddress).filter(models.UserAddress.user_id == user.id)
    address = query.first()

    if query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id({id}) does not exist")

    if address.id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized to perfrom requested action")
    return address