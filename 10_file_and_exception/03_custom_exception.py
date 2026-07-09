class OutOfIngrediantsError(Exception):
    pass

def make_chai(milk,suger):
    if milk == 0 or suger == 0:
        raise OutOfIngrediantsError("milk and suger must be provided!")
    print("chai is ready!")

make_chai(0,5)
make_chai(3,0)
make_chai(2,2)