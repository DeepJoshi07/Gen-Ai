from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address

add = Address(street="cold street",city="woshington",postal_code="382424")

user = User(id=12,name="deep",address=add)

print(user)

# or

user2 = {
    "id":12,
    "name":"deep",
    "address":{
        "street":"cold street",
        "city":"woshington",
        "postal_code":"382424"
    }
}

u1 = User(**user2)
print(u1)