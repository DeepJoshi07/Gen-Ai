# Global interpreter lock
# mutex

from threading import Thread,current_thread
import time

def make_chai():
    print(f"making chai for #{current_thread().name}.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"chai for #{current_thread().name} has been made.")


b1 = Thread(target=make_chai,name="Barista-1")
b2 = Thread(target=make_chai,name="Barista-2")

start = time.time()

b1.start()
b2.start()

b1.join()
b2.join()

end = time.time()

print(f"the time has taken to make chai is: {end-start:.2f} seconds")