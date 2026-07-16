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

# async def main():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor(max_workers=2) as pool:
#         # Submit 3 tasks but only 2 threads available
#         tasks = [
#             loop.run_in_executor(pool, check_stock, "chai"),
#             loop.run_in_executor(pool, check_stock, "coffee"),
#             loop.run_in_executor(pool, check_stock, "sugar"),
#         ]
#         results = await asyncio.gather(*tasks)
#         print(results)


asyncio.run(main())