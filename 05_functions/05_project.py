def chai_report():
    return 15,30,["masala"]

price1,price2,chai_type = chai_report()

print(price1)
print(price2)
print(chai_type)

p1,_,_= chai_report()

print(p1)

print("----------------------------------------------------")

# pure and impure function

chai_cups = 12

def pure_chai(cups,price):
    return cups * price

def impure_chai(cups,price):
    global chai_cups
    chai_cups += cups
    return chai_cups * price

print(pure_chai(10,15))

# function that manipulates global variable known as impure function

print(impure_chai(10,15)) # not recommended

print("------------------------------------------")

# recursive

def print_nums(num):
    if num == 0: 
        return
    print_nums(num-1)
    print(num)

print_nums(10)

print("-----------------------------------")

# lemda function

nums = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda num : num % 2 == 0,nums))

print(even)