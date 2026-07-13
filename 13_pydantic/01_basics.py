from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    height:int


user = {
    "name":"deep",
    "age":23,
    "height":180
}

my_user = User(**user)

print(my_user)