from pydantic import BaseModel,computed_field,Field

class Product(BaseModel):
    price:int
    quantity:int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

p1 = Product(price=20000,quantity=13)
print(p1)

class Booking(BaseModel):
    id:int
    room_id:int
    nights : int = Field(...,ge=1)
    per_night_price : int

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.per_night_price * self.nights
    
b1 = Booking(id=123,room_id=456,nights=4, per_night_price=12000)
print(b1)
print(b1.model_dump())
print(b1.model_dump_json())