from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

from ..database import  get_db
from .. import models, responses, schemas, utils, oauth2
#


router = APIRouter(
    prefix= "/products",
    tags=['Products']
)

@router.post("/", response_model=responses.ProductResponse)
def create_product(product: schemas.ProductBase ,db: Session =Depends(get_db)):
    new_product = models.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
    pass


@router.get("/", response_model=List[responses.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Products).all()

    return products


@router.get("/{id}", response_model=responses.ProductResponse)
def get_produce(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Produce with id({id}) does not exist")
    return product


@router.put("/{id}", response_model=responses.ProductResponse)
def update_produce(id: int, updated_prod: schemas.ProductBase, db: Session = Depends(get_db)):
    query = db.query(models.Products).filter(models.Products.id == id)
    product = query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Produce with id({id}) does not exist")

    # if product.admin != user.username:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#     #                         detail="Not authorized to perfrom requested action")

    query.update(updated_prod.dict(), synchronize_session=False)

    db.commit()
    return query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_produce(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Products).filter(models.Products.id == id)
    product = query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"farm with id({id}) does not exist")

#     # if produce.farm != user.username:
#     #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#     #                         detail="Not authorized to perfrom requested action")

    query.delete(synchronize_session=False)
    db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)
