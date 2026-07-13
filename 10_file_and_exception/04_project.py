class InvalidChaiError(Exception): pass

def bill(flavor,cups):
    menu = {"masala":20,"ginger":30}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Given chai is not available.")
    
        if not isinstance(cups,int):
            raise ValueError("cups must be in numbers not string!")
    
        total = menu[flavor] * cups

        print("Your total is :",total)

    except Exception as e:
        print("Error :",e)
    finally:
        print("Thank you for visiting us!")

print("-----------------------------------")
bill("tulsi",5)
print("-----------------------------------")
bill("ginger","two")
print("-----------------------------------")
bill("masala",4)