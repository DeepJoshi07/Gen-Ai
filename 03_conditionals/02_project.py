order_price = int(input("Enter Order price: "))

delivery_fees = 0 if order_price > 300 else  30

print("delivery fees is :",delivery_fees)