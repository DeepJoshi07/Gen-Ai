from multiprocessing import Process
import time

def make_chai(name):
    print(f"making chai #{name}.")
    time.sleep(3)
    print(f"the #{name} chai has been made.")

if __name__ == "__main__":
    all_chais = [
        Process(target=make_chai,args=(f"process number #{i}",))
        for i in range(3) 
    ]

    for p in all_chais:
        p.start()

    for p in all_chais:
        p.join()

    print("proccess has ended.")