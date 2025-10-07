from functools import wraps
import time

def timing(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)   # await async function
        end_time = time.time()
        print (f"function took {end_time - start_time:.5f}s")
        return result
    return wrapper