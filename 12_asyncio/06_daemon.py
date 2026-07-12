from threading import Thread
import time

print("--------------------- while daemon is True ------------------")
# def chai_temp():
#     while True:
#         print("measuring chai temprature....")
#         time.sleep(2)

# Thread(target=chai_temp,daemon=True).start()

# print("programme is executed.")

print("--------------------- while daemon is False ------------------")

def chai_temp():
    while True:
        print("measuring chai temprature....")
        time.sleep(2)

Thread(target=chai_temp,).start()

print("programme is executed.")