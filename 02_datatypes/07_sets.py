essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(all_spices)

comman = essential_spices & optional_spices
print(comman)

only_in_essential = essential_spices - optional_spices
print(only_in_essential)

# membership
print("cloves" in optional_spices)