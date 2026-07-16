from threading import Thread,Lock
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

threads = [Thread(target=cpu_havy) for _ in range(2)]

start = time.time()

[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()

print(f"total time taken is: {end-start:.2f}")