tempreture = 40 

while tempreture < 101:
    print(f"tempreture is {tempreture} degrees")
    tempreture += 15

print("water is boiling add tea leaves in it.")

# continue, break

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
i = 0
while(i < len(nums)):
    if nums[i] % 2 == 0:
        i+=1
        continue
    if nums[i] == 11:
        break
    print(f"your number is : {nums[i]}")
    i += 1