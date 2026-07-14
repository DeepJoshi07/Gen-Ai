from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime

class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    subscription_price:int

    start_date:datetime
    end_date:datetime

    @field_validator("fist_name","last_name")
    def validate_names(cls,v):
        if not v.istitle():
            raise ValueError("first_name and last_name must be in capital.")
        return v
    
    @field_validator('email')
    def normalize_email(cls,v):
        return v.lower().strip()
    
    @field_validator('subscription_price',mode='before')
    def parse_price(cls,v):
        if isinstance(v,str):
            return float(v.replace('$',''))
        return v
    
    @model_validator(mode='after')
    def validate_subscription(cls,vals):
        if vals.start_date <= vals.end_date:
            raise ValueError("end date must come after start date.")
        return vals