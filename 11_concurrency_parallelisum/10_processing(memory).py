from multiprocessing import Process,Value,Queue


def increament(counter):
    print("counting started.")
    with counter.get_lock():
        for _ in range(100_000_00):
            counter.value += 1
    print("counting is done.")

if __name__ == "__main__":
    counter = Value('i',0)

    processes = [Process(target=increament,args=(counter,)) for _ in range(3)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print(counter.value)