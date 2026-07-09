def process_order(item,qty):
    try:
        price = {"masala":20}[item]
        cost = price * qty
        if type(cost) != int:
            raise ValueError("provided value must be number.")
        print("Your chai cost is:",cost)
    except KeyError:
        print("Provided item is not in stock!")
    except ValueError as v:
        print(v)

process_order("ginger",2)
print("-----------------------------")
process_order("masala","three")
print("-----------------------------")
process_order("masala",3)