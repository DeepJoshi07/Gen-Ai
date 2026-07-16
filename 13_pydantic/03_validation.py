from pydantic import BaseModel,Field 
from typing import Optional

class Employee(BaseModel):
    id:int
    name: str = Field(
        ...,
        max_length=50,
        min_length=3,
        description="employees full name must be added."
    )
    age:int = Field(
        ...,
        gt=17,
        lt=60
    )
    salary : int = Field(
        ...,
        gt=10000,
        description="salary must be more then 10,000."
    )
    address: Optional[str] = Field(
        default=None,
        description="address must include street block no and zip."
    )

e1 = Employee(id=12,name="jayesh",age=23,salary=20000,address="nahi hai.")
e2 = Employee(id=12,name="jayesh",age=23,salary=20000,)
print(e1)
print(e2)
