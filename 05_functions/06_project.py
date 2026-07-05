# built-in functions

def chai_order(chai):
    """this function prints the chai name you provide"""
    print(f"You have orderd {chai} chai.")

print("Functions purpose :",chai_order.__doc__)
print("Function name :",chai_order.__name__)

help(len)