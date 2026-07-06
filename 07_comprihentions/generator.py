prices = [15,20,30,40,50,80,100]

high_price = (p for p in prices)

print(high_price)

high_price = sum(p for p in prices)

print(high_price)

# unlike list in generator value comes as a flow in memory

# this is highly memory efficient

# it yeilds the value which we wii understand in following section