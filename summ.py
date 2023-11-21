import asyncio
import time

async def summ(a, b):
    await asyncio.sleep(1)
    print(a + b)

async def slow(a, b):
    await asyncio.sleep(5)
    print(a * b)

async def main():
    start = time.time()
    task1 = asyncio.create_task(summ(12, 3))
    task2 = asyncio.create_task(slow(2, 5))
    await task1
    await task2
    en = time.time()
    print(en - start)

asyncio.run(main())