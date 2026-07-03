size = input("enter the chai size [small/midium/large] :").lower()

if size == "small":
    print("your total is 1.20$")
elif size == "midium":
    print("your total is 1.80$")
elif size == "large":
    print("your total is 2.00$")
else:
    print("invalid size")