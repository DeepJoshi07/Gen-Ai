class Chai:
    def __init__(self,type_):
        self.type = type_

    def print_chai_type(self):
        return f"your chai is {self.type}."
    
class Masala(Chai):
   price = 45
   is_spicy = True

   def make_chai(self):
       return "making masala chai"
   
   def print_chai_type(self):
       return f"your chai type is {self.type} and price is {self.price}"

masala = Masala(45)

print(masala.print_chai_type())
print(masala.price)

print("------------------------------------------")
# composition

class Ginger:
    price = 35
    chai_base = Chai
    def __init__(self,type_):
        self.chai = self.chai_base(type_)

ginger = Ginger("Spicy")

print(ginger.chai.print_chai_type())
print(ginger.price)

print("-----------------------------------------------")

class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def spices(self):
        return ["milk","suger","tea leaves"]

class Masala(BaseChai):
    def make_chai(self):
        return "making masala chai"


class ChaiShop:
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Reguler")
    
    def serve(self):
        return f"serving reguler chai"

class FancyShop(ChaiShop):
    chai_cls = Masala


main_chai = FancyShop()
print(main_chai.chai.make_chai())
print(main_chai.chai.spices())
print(main_chai.chai.type)