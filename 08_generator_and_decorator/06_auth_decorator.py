from functools import wraps

def authentication(fnc):
    @wraps(fnc)
    def wrapper(user_role):
        if user_role == "admin":
            return fnc(user_role)
        else:
            print("access not granted")

    return wrapper

@authentication
def change_inventory(user_role):
    print("Access has been granted to the user.")

change_inventory("admin")
print("--------------------------------------")
change_inventory("user")