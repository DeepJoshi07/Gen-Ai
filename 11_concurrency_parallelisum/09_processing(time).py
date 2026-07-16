from multiprocessing import Process,Lock
import time

lock = Lock()

# def cpu_havy():
#     print("process has started.")
#     with lock:
#         total = 0
#         for _ in range(10**8):
#             total+=1
#     print("Done.")

def cpu_havy():
    print("process has started.")
    total = 0
    for _ in range(10**8):
        total+=1
    print("Done.")

if __name__ == "__main__":

    processes = [Process(target=cpu_havy) for _ in range(2)]

    start = time.time()

    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()

    print(f"total time taken is: {end-start:.2f}")