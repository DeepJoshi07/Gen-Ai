ordered_chais = [
    "Masala Chai","lemon tea","ginger chai","clove tea",
    "Masala Chai","lemon tea"
]

unique_chais = {tea for tea in ordered_chais}

print (unique_chais)

unique_chais = {tea for tea in ordered_chais if len(tea) < 10}

print(unique_chais)

recipes = {
    "masala chai":["ginger","cardamom","clove"],
    "elichi chai":["cardamom","milk"],
    "spicy chai":["pepper","ginger","clove"]
}

all_ingrediants = {spice for ingrediants in recipes.values() for spice in ingrediants}

print(all_ingrediants)