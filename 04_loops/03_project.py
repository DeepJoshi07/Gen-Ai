# walrus  operator

value = 23
remandor = 23 %  5

if remandor:
    print("there is a remendor!")

val = 23

if (rem := val % 5):
    print("there is a remandor!")

available_sizes = ["small","medium","large"]

if (size := input("enter the chai size : ")) in available_sizes:
    print(f"serving {size} size chai!")
else:
    print("unavailable size!")

flavors = ["ginger","lemon","mint","masala"]

print("available flavors : ",flavors)

while(option := input("enter your flaor : ")) not in flavors:
    print(f"sorry, your chosen flavor {option} is not available.")

print("your chai has been made!")