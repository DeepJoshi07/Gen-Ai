def calculate_bill(cups,price):
    return cups*price

result = calculate_bill(5,15)

print(f"the price to be paid : ",result)

print("-----------------------------------------")

def add_GST(price,rate):
    return price * (100 + rate)/100

bill = [100,120,250,500]

for amount in bill:
    amount_with_gst = add_GST(amount,18)
    print(f"Your total amount with gst is : ",amount_with_gst)

