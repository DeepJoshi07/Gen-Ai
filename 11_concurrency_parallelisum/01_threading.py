import threading
import time

def brew_chai():
    for i in range(1,4):
        print(f"brewing chai #{i}.")
        time.sleep(3)

def make_chai():
    for i in range(1,4):
        print(f"making chai #{i}.")
        time.sleep(2)

# threading

make_chai_thread = threading.Thread(target=make_chai)
brew_chai_thread = threading.Thread(target=brew_chai)

make_chai_thread.start()
brew_chai_thread.start()

make_chai_thread.join()
brew_chai_thread.join()