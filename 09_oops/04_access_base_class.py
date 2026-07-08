class Chai:
    def __init__(self,type_,milk):
        self.type = type_
        self.milk = milk

class Cardamom(Chai):
    def __init__(self, type_, milk,suger):
        self.type = type_
        self.milk = milk
        self.suger = suger
        

class Masala(Chai):
    def __init__(self, type_, milk,suger):
        Chai.__init__(self,type_,milk)
        self.suger = suger

class Ginger(Chai):
    def __init__(self, type_, milk, suger):
        super().__init__(type_, milk)
        self.suger = suger

# method resolution order

class A:
    label = "class A label"

class B(A):
    label = "class B label"

class C(A):
    label = "class C label"

class D(B,C):
    pass

label = D()
print(D.label)