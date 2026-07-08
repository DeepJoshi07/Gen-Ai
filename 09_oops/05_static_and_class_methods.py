# static methods

class MakeList:
    @staticmethod
    def list_making(text):
        return [item.strip() for item in text.split(",")]
    
random_str = "deep,meet , heer,  jay  , harsh "

name_list = MakeList.list_making(random_str)

print(name_list)

print("-------------------------------------------------")
# classmethod

class ChaiOrder:
    def __init__(self,chai_type,sweetness,size):
        self.chai_type = chai_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def init_dict(cls,dictionary_obj):
        return cls(
            dictionary_obj["chai_type"],
            dictionary_obj["sweetness"],
            dictionary_obj["size"]
        )
    
    @classmethod
    def init_string(cls,string_val):
        chai_type,sweetness,size = string_val.split(",")
        return cls(
            chai_type,
            sweetness,
            size
        )
    
order1 = ChaiOrder.init_dict({
    "chai_type":"ginger",
    "sweetness":"midium",
    "size":"large"
})

print(order1.chai_type)
print(order1.sweetness)
print(order1.size)

print("------------------------------------------------")

order2 = ChaiOrder.init_string("lemon,high,small")

print(order2.chai_type)
print(order2.sweetness)
print(order2.size)

print("-------------------------------------------------")

order3 = ChaiOrder("masala","low","midium")

print(order3.chai_type)
print(order3.sweetness)
print(order3.size)