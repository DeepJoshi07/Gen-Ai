# deadlock

from threading import Thread,Lock

t1 = Lock()
t2 = Lock()

def task1():
    with t1:
        print("lock 1 is done.")
        with t2:
            print("lock 2 is done")

def task2():
    with t2:
        print("lock 3 is done.")
        with t1:
            print("lock 4 is done")

thread1 = Thread(target=task1)
thread2 = Thread(target=task2)

thread1.start()
thread2.start()
