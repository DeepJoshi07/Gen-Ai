from threading import Thread
import time
import asyncio

def bg_worker():
    while True:
        time.sleep(1)
        print("loging the system health.")

async def fetch_orders():
    await asyncio.sleep(3)
    print("Orders fetched.")

Thread(target=bg_worker,daemon=True).start()

asyncio.run(fetch_orders())