def chai_customer():
    print("what chai would you like ?")
    order = yield
    while(True):
        print("Preparing",order)
        order = yield

stall = chai_customer()

next(stall)

stall.send("masala chai")
stall.send("lemon tea")
stall.send("elichi chai")