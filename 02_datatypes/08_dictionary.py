# union insertion also exists in dictionary

chai_order = dict(
    type="masala chai",
    size="large",
    suger=2
)
print(chai_order)
print(chai_order["size"])

chai_order2 = {
    "type":"masala chai",
    "size":"large",
    "suger":2
}
print(chai_order2)
print(chai_order2["suger"])

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(chai_recipe)
print(chai_recipe["base"])
del chai_recipe["liquid"]
print(chai_recipe)

# membership

print("suger" in chai_order)

print(f"keys in chai order : {chai_order.keys()}")
print(f"values in chai order : {chai_order.values()}")
print(f"items in chai order : {chai_order.items()}")

last = chai_order.popitem() # pop can also be used but it doesn't return anything
print(last)

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)
print(chai_recipe)

print(chai_order["size"]) #  not safe
print(chai_order.get("note","there is no note")) # safe