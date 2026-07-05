# scops and name resolution
# local
# global
# enclosing from outer function if nested
# built in

def serve_chai():
    chai_type = "masala" # local scop
    print(f"your chai is {chai_type} chai.")

chai_type = "ginger" # global scop

serve_chai()

print(f"your chai is {chai_type} chai.")

print("-------------------------------------------------")

def chai_counter():
    chai_type2 = "lemon"
    def print_chai():
        chai_type2 = "cardamom" # Enclosing scop
        print("Inner function", chai_type2)
        print("---------")
        print(chai_type) # global
        print("---------")
    print_chai()
    print("Outer function", chai_type2)
    print("---------")
    print(chai_type) # global
    print("---------")

chai_type2 = "tulsi"

chai_counter()

print("Global scop",chai_type2) # global

# non-local vs global scop

print("-----------------------------------")

def update_order():
    chai_order = "clove"
    def kitchen():
        nonlocal chai_order
        # just for one step above not global
        chai_order = "keser"
        print(chai_order)
    kitchen()
    print(chai_order)

update_order()

print("------------------------------------")

chai_order = "random"

def update_order():
    
    def kitchen():
        # nonlocal chai_order # gives error
        global chai_order
        chai_order = "cinamon"
        print(chai_order)
    kitchen()
    print(chai_order)

update_order()
print(chai_order)