class Human:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
        return
    
h1 = Human(23)
print(h1.age)
h1.age = 25
print(h1.age)