def make_chai(chai_type,milk,suger):
    print(f"your {chai_type} chai with milk [{milk}] and suger [{suger}].")

make_chai("ginger",True,"midium") # Arguments in order

make_chai(suger="high",chai_type="keser",milk=True) # Arguments the way we want

print("------------------------------------")

# Arguments and key-word Arguments
# * arguments(tuple)
# ** dictionary

def make_chai2(*ingrediants,**kw_ingrediants):
    print("Ingrediants",ingrediants)
    print("KW Ingrediants",kw_ingrediants)

make_chai2("tulsi","keser","clove",milk=True,suger="high",hot=False)

# default trap

print("-------------------------------------------")

def chai_order(order=[]):
    order.append("masala")
    print(order)

chai_order()
chai_order()

print("------------")

def chai_order2(order=None):
    if order is None:
        order = []
    print(order)

chai_order2()
chai_order2(["lemon"])