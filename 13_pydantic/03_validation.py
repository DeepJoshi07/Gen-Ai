from pydantic import BaseModel,Field

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
    salary = int = Field(
        ...,
        gt=10000,
        description="salary must be more then 10,000."
    )
