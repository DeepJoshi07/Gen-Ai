from threading import Thread
import time

def make_cream(span):
    print("making cream....")
    time.sleep(span)
    print("cream has been made")

def make_cake(span):
    print("Making cake....")
    time.sleep(span)
    print("cake has been made.")

t1 = Thread(target=make_cream,args=(3,))
t2 = Thread(target=make_cake,args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()
