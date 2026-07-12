import asyncio

# co-routin
async def make_chai(name):
    print(f"making {name} chai.")
    await asyncio.sleep(3)
    print(f"your {name} chai is ready.")

async def main():
    await asyncio.gather(
        make_chai("masala"),
        make_chai("ginger"),
        make_chai("cardamom")
    )

asyncio.run(main())