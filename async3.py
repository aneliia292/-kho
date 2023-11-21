import asyncio
import time

async def makeCoffee():
    print('start makeCoffee')
    await asyncio.sleep(3)
    print('end makeCoffee')
    return 'Coffee is ready'

async def toastBrew():
    print('start toastBrew')
    await asyncio.sleep(2)
    print('end toastBrew')
    return 'toast is ready'

async def main():
    start = time.time()
    work = asyncio.gather(makeCoffee(), toastBrew())
    res_coffee, res_toast = await work
    end = time.time()
    print(res_coffee)
    print(res_toast)
    print(f'Времени прошло {end-start:.2f} минут')


if __name__ == '__main__':
    asyncio.run(main())
