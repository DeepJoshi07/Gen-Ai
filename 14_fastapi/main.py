from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from sqlalchemy.orm import Session
from database import session,engine
from db_model import Base
import db_model

Base.metadata.create_all(bind=engine)

products = [
    Product(id=1,name="laptop",description="this is the laptop.",price=60000,quantity=10),
    Product(id=2,name="mobile",description="this is the mobile.",price=20000,quantity=15),
    Product(id=3,name="ac",description="this is the ac.",price=40000,quantity=12),
    Product(id=4,name="tv",description="this is the tv.",price=15000,quantity=17),
    Product(id=5,name="fridge",description="this is the fridge.",price=35000,quantity=20),
]

def init_db():
    db = session()
    count = db.query(db_model.Product).count
    if count == 0:
        for product in products:
            db.add(db_model.Product(**product.model_dump()))

    db.commit()

init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000/"],
    allow_methods = ["*"],
)

@app.get("/")
def greet():
    return "hello first user."



@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    # return products
    db_products = db.query(db_model.Product).all() 
    return db_products



@app.get("/product/{id}")
def get_product_by_id(id:int,db:Session = Depends(get_db)):
    # for product in products:
    #     if product.id == id:
    #         return product
    product_db = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if product_db:
        return product_db
    return "Product not Found!"



@app.post("/product")
def add_product(product:Product,db: Session = Depends(get_db)):
    # products.append(product)
    new_product = db_model.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)   # <-- pulls DB-assigned fields like id
    return new_product



@app.put("/product")
def update_product(id:int,product:Product,db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "Product updated succesfully!"
    db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        return "Product not found."



@app.delete("/product")
def delete_product(id:int,db : Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return "Product deleted successfully!"
    product_db = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if product_db :
        db.delete(product_db)
        db.commit()
        return "Product deleted"
    else:
        return "Product not Found!"