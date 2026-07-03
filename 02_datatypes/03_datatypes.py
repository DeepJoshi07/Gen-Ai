# integer
# arithmetic operations
# logical operations [and, or, not]
# (-), (+), (/), (//), (*), (**)
# readability (_)
# boolean (false -> None, "", 0), (true -> 1,2...n,"str", )

fruits = 12
sold = 5
print("----- subtraction -----")
left = fruits - sold
print(f"fruits left is {left}")

buy = 23
print("----- addition -----")
print(f"total fruites after buying new ones :{left+buy}")
total_fruits = left + buy

children = 4
print("----- division -----")
print(f"each child gets {total_fruits/4} fruits")
print("------------------ without prisision -------------------")
print(f"each child gets {total_fruits//4} fruits")
print("----------------------------------")


print("----- remandor -----")
print(f"fruits left {total_fruits%children}")

print("----- Power ------")
print(3**5)

print("----- another way to write a number")
# for radability
ran_num = 1_000_000_000
print(ran_num)

print("-------------------- Boolean -------------------------")
is_num = True # 1
num = 12
print(is_num+num) # up casting
is_num = False # 0 None is also 0
print(is_num+num)
print(bool(None)) # false
print(bool(0)) # false
print(bool(1)) # true
print(bool(11)) # true
print(bool("")) # false
print(bool("deep")) # true

print("----------------------- logical operator -----------------------")
hot_water = False
cold_water = True

warm_water = hot_water and cold_water

print(warm_water)

warm_water = hot_water or cold_water

print(warm_water)

warm_water = not(hot_water and cold_water)

print(warm_water)

