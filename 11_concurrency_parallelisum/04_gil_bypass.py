from multiprocessing import Process
import time

def make_chai():
    print(f"making chai has started.")
    count = 0
    for _ in range(100_000_000): count+=1
    print(f"the chai has been made.")

if __name__ == "__main__":
    p1 = Process(target=make_chai)
    p2 = Process(target=make_chai)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    
    print(f"total time taken to make chai is {end-start:2f}.")