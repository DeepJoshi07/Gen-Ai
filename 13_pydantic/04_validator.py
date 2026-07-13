from pydantic import BaseModel,field_validator, model_validator

class User(BaseModel):
    username:str

    @field_validator("username")
    def validate_username(cls,name):
        if(len(name) < 3):
            raise ValueError("Name length must be 3 or bigger.")
        return name
    
user = User(username="deep")

print(user)

class SignupData(BaseModel):
    password:int
    confirm_pass:int

    @model_validator(mode="after")
    def validate_pass(cls,vals):
        if vals.password != vals.confirm_pass:
            raise ValueError("Passwords do not match")
        return vals


data = SignupData(password=1234,confirm_pass=1234)
print(data) 
