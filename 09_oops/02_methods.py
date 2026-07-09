class Chai:
    origin = "india"

    def describe(self):
        return(f"this chai originated in {self.origin}")
    

masala = Chai()
print(masala.describe())
print(Chai.describe(masala))
masala.origin = "Nepal" 
print(masala.origin)
print(Chai.origin)

print("----------------------------------------------------")
# constroctor

class ChaiOrder:
    def __init__(self,type_,price):
        self.type = type_
        self.price = price

    def self_print(self):
        return(f"the chai you ordered is {self.type} and price is {self.price}")
    
lemon2 = ChaiOrder("lemon2",70)
print(lemon2.self_print())

lemon = ChaiOrder("lemon",50)
print(lemon.self_print())

print(lemon2.self_print())