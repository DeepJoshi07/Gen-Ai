def chai_types():
    yield "masala"
    yield "ginger"
    yield "clove"

chai_options = chai_types()

print(chai_options)

for chai in chai_options:
    print(chai)

print("-------------------------------------")

def get_chai_list1():
    return ["cup1","cup2","cup3","cup4"]

all_chais1 = get_chai_list1()

print(all_chais1)

for chai in all_chais1:
    print(chai)

print("--------------------------------")

def get_chai_list2():
    yield "cup1"
    yield "cup2"
    yield "cup3"
    yield "cup4"

all_chais2 = get_chai_list2()

print(get_chai_list2)

for chai in all_chais2:
    print(chai)

print("-------------------------------------")

all_chais3 = get_chai_list2()

print(next(all_chais3))
print(next(all_chais3))
print(next(all_chais3))
print(next(all_chais3))