import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(item):
    return item[::-1]

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,encrypt,"my_credit_card")
        print(result)

asyncio.run(main())