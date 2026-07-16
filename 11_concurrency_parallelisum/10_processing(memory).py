from multiprocessing import Process,Value,Queue
import time

def increament(counter):
    print("counting started.")
    with counter.get_lock():
        for _ in range(100_000_00):
            counter.value += 1
    print("counting is done.")

if __name__ == "__main__":
    counter = Value('i',0)

    processes = [Process(target=increament,args=(counter,)) for _ in range(3)]

    start = time.time()

    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()

    print(counter.value)
    print(f"total time taken is: {end-start:.2f}")