from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from .. import schemas, models, utils, oauth2, responses

router=APIRouter(
    tags=['Authentication']
)



# @router.post("/login/admin", response_model=responses.Token)
# def login_farmer(login_credentials:OAuth2PasswordRequestForm= Depends(), db:Session = Depends(get_db), ):

#     admin = db.query(models.Admin).filter(models.Admin.username == login_credentials.username).first()

#     if not admin:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    
#     if not utils.authentication(login_credentials.password, farm.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    
#     access_token = oauth2.create_access_token(data = {"admin_username": admin.username})

#     return {"access_token": access_token, "token_type":"bearer"}

@router.post("/login_user", response_model=responses.Token)
def login_user(login_credentials:OAuth2PasswordRequestForm= Depends(), db:Session = Depends(get_db)):

    user = db.query(models.Users).filter(models.Users.username == login_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    
    if not utils.authentication(login_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access_token": access_token, "token_type":"bearer"}



 