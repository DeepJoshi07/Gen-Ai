# for in range loop
# works on any iterable arr, string, dictionary, set,.. etc.

for token in range(1,11):
    # last number is not inclusive
    print(f"chai is ready for token number #{token}")

random_list = ["deep","herpreet","jaimin","jimmy","smrity"]

for name in random_list:
    print(f"the name is : {name}")

random_string = "hello world"

for char in random_string:
    print(f"your character is : {char}")

random_dict = {
    "name":"deep",
    "age":23,
    "marks":99,
    "height":180
}

for prop in random_dict:
    print(f"your key is : {prop}")
    print(f"your value is : {random_dict[prop]}")

random_set = {1,2,3,4,5,6,7,8}

for num in random_set:
    print(num)

for idx,name in enumerate(random_list,start=1):
    print(f"rank {idx} : {name}")

rupees = [100,90,80,70,60,50]

for name,money in zip(random_list,rupees):
    print(f"{name} paid {money} only.")