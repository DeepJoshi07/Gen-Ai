import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"checking stock for {item}.")
    time.sleep(3)
    return f"the stock for {item} is 42."

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,check_stock,"masala chai")
        print(result)

asyncio.run(main())