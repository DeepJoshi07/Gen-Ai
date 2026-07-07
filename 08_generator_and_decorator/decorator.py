from functools import wraps

def my_decorator(fnc):
    @wraps(fnc)
    def wrapper():
        print("before function runs")
        fnc()
        print("after function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello there!")

greet()
print(greet.__name__)

print("------------------------------------------------------")

def log_activity(fnc):
    @wraps(fnc)
    def wrapper(*args,**kwargs):
        print(f"calling :{fnc.__name__}")
        result = fnc(*args,**kwargs)
        print(f"called :{fnc.__name__}")
        return result
    return wrapper

@log_activity
def chai_order(name,milk,suger):
    print(f"your chai {name} is ready with milk status {milk} and suger level {suger}.")

chai_order("masala chai",milk=False,suger="midium")