file = open("order.txt","w")

try:
    file.write("hello world! good to see you.")
finally:
    file.close()

with open("order2.txt",'w') as file:
    file.write("hello world again!, and good to see you.")