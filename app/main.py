
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, products, auth, user_cart, create_cart, user_address

#
#

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# #Linking routes in routers to FastApi
app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(user_cart.router)
app.include_router(create_cart.router)
app.include_router(user_address.router)


# app.include_router()
# app.include_router()


@app.get("/")
def root():
    return {"message": "Hello World"}
