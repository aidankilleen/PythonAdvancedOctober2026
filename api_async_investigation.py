# api_async_investigation.py

import asyncio
import httpx
import time
from tqdm.asyncio import tqdm

#from async_timing_decorator import timing

urls = ["https://api.acodingtutor.com/users/1082?_delay=5000", 
        "https://api.acodingtutor.com/users/1084?_delay=2000"]

async def fetch(client, url):
    resp = await client.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

async def progress(seconds):
    with tqdm(total=seconds, desc="Downloading data", unit="s") as pbar:
        for i in range(seconds):
            await asyncio.sleep(1)
            pbar.update(1)


async def main():

    async with httpx.AsyncClient() as client:
        #start_time = time.time()
        t1 = asyncio.create_task(fetch(client, urls[0]))
        t2 = asyncio.create_task(fetch(client, urls[1]))
        pb = asyncio.create_task(progress(5))
        data1, data2, x = await asyncio.gather(t1, t2, pb)

        print (data1)
        print (data2)
        
        #end_time = time.time()
        #print (f"function took {end_time - start_time:.5f}s")

asyncio.run(main())
