from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    height:int
    is_heavy:bool = False


user = {
    "name":"deep",
    "age":23,
    "height":180
}

my_user = User(**user)
my_user2 = User(**user,is_heavy=True)

print(my_user)
print(my_user2)