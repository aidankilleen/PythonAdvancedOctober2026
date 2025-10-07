# async_investigation.py

import asyncio

# define an asynchronous function
async def worker(title, delay):
    for i in range(10):
        print (f"{title} {i}")
        await asyncio.sleep(delay)

async def main():
    t1 = asyncio.create_task(worker("worker1", 1.2))
    t2 = asyncio.create_task(worker("worker2", 0.7))
    t3 = asyncio.create_task(worker("worker3", 0.25))

    await asyncio.gather(t1, t2, t3)

# start the asynchronous function
asyncio.run(main())

print("finished")