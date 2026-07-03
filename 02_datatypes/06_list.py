# append(item), remove(item), insert(idx,item), extand, pop, 
# reverse, sort, max, min

ingredients = ["water","milk","black tea"]
ingredients.append("suger")
print(f"Ingredients are :{ingredients}")

ingredients.remove("water")
print(f"Ingredients are :{ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"chai : {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"chai : {chai_ingredients}")

last = chai_ingredients.pop()
print(last)
print(chai_ingredients)

chai_ingredients.reverse()
print(chai_ingredients)

chai_ingredients.sort()
print(chai_ingredients)

sugar_level = [1,2,3,4,5,6]
print(f"max : {max(sugar_level)}")
print(f"min : {min(sugar_level)}")

# operator overloading

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(full_liquid_mix)

print(base_liquid * 3)

# bytearray  
data = bytearray(b"CINNAMON")
print(data)
new_data = data.replace(b"CINNA",b"CARD")
print(new_data)