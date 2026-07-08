class Chai:
    origin = "india"

class ChaiTime:
    pass

print(type(Chai))

new_chai = Chai()

print(type(new_chai))
print(type(new_chai) is Chai)
print(type(new_chai) is ChaiTime)

print("-----------------------------------")
# adding values explicitly

Chai.is_hot = True

print(Chai.is_hot)

masala = Chai()

masala.suger = "midium"

print(masala.is_hot)
print(masala.suger)

try:
    print(Chai.suger)
except:
    print("suger property does not exists in Chai class.")

print("-------------------------------------")
#  deleting attributes in class

ginger = Chai()

ginger.origin = "Nepal"

print(ginger.origin)

del ginger.origin

print(ginger.origin)

ginger.is_spicy = False

print(ginger.is_spicy)

del ginger.is_spicy

# print(ginger.is_spicy)
# gives error because the is_spicy property never existed in Chai class
# origin do not get error because it originlly existed in Chai class