from typing import List
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

from ..database import get_db
from .. import models, responses, schemas, utils, oauth2
#


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=responses.Users)
def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.Users(**user.dict())
    if new_user != None:
        raise HTTPException(status.HTTP_306_RESERVED, detail="User details already exist")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=List[responses.Users])
def get_all_users(db:Session=Depends(get_db)):

    users = db.query(models.Users).all()

    return users


@router.get("/{id}", response_model=responses.Users)
def get_farm(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exist")

    return user


@router.put("/{id}", response_model=responses.Users)
def update_user(id: int, updated_user: schemas.Users, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Users).filter(models.Users.id == id)
    user = query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Produce with id({id}) does not exist")
    if user.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized to perfrom requested action")

    query.update(updated_user.dict(), synchronize_session=False)
    db.commit()
    return {"data": query.first()}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Users).filter(models.Users.id == id)
    user = query.first()
    if query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"farm with id({id}) does not exist")
    if user.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized to perfrom requested action")
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
