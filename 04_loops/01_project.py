# for in range loop
# works on any iterable arr, string, dictionary, set,.. etc.

for token in range(1,11):
    # last number is not inclusive
    print(f"chai is ready for token number #{token}")

print("-------------------------------------")

random_list = ["deep","herpreet","jaimin","jimmy","smrity"]

for name in random_list:
    print(f"the name is : {name}")

print("-------------------------------------")

random_string = "hello world"

for char in random_string:
    print(f"your character is : {char}")

print("-------------------------------------")

random_dict = {
    "name":"deep",
    "age":23,
    "marks":99,
    "height":180
}

for prop in random_dict:
    print(f"your key is : {prop}")
    print(f"your value is : {random_dict[prop]}")

print("-------------------------------------")

random_set = {1,2,3,4,5,6,7,8}

for num in random_set:
    print(num)

print("-------------------------------------")

for idx,name in enumerate(random_list,start=1):
    print(f"rank {idx} : {name}")

print("-------------------------------------")

rupees = [100,90,80,70,60,50]

for name,money in zip(random_list,rupees):
    print(f"{name} paid {money} only.")

print("-------------------------------------")

# for else 
# works only when the for loop doesn't break

workers = [("deep",23),("meet",16),("jay",18),("mehul",15)]
workers2 = [("deep",23),("meet",16),("jay",18),("mehul",16)]

for name,age in workers:
    if age == 15:
        print(f"worker {name} is not eligible.")
        break
    print(f"worker {name} is eligible to work.")
else:
    print("no break statement came.")

print("-------------------------------------")

for name,age in workers2:
    if age == 15:
        print(f"worker {name} is not eligible.")
        break
    print(f"worker {name} is eligible to work.")
else:
    print("no break statement came.")