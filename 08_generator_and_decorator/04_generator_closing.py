def indian_chai():
    yield "masala chai"
    yield "elichi chai"
    yield "ginger chai"

def foreign_chai():
    yield "lemon tea"
    yield "macha"
    yield "Oolong"

def all_chais_menu():
    yield from indian_chai()
    print("------------")
    yield from foreign_chai()

chais = all_chais_menu()

for chai in chais:
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order."
    except:
        print("there was no chai order!")

stall = chai_stall()

print(next(stall))

stall.close()
