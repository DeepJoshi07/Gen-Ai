from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    item_name:str
    item_size:List[int]
    item_color:Dict[str,str]
    item_width:Optional[int] = None

item = Cart(item_name="T-shirt",item_color={"red":"dark","blue":"light"},item_size=[20,30,40,50],)

item2 = Cart(item_name="T-shirt",item_color={"red":"dark","blue":"light"},item_size=[20,30,40,50],item_width=45)

print(item)
print(item2)