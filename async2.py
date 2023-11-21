import time
import asyncio


async def count(counter):
    print(f'Количество записей в списке {len(counter)}')
    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)

async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'Прошла 1 секунда. Элементов в списке {len(counter)}')


async def print_every_5sec():
    while True:
        await asyncio.sleep(5)
        print(f'Прошла 5 секунд')


async def print_every_10sec():
    while True:
        await asyncio.sleep(5)
        print(f'Прошло 10 секунд')


async def main():
    counter = list()
    task1 = asyncio.create_task(count(counter))
    task2 = asyncio.create_task(print_every_sec(counter))
    task3 = asyncio.create_task(print_every_5sec())
    task4 = asyncio.create_task(print_every_10sec())

    task_list1 = [task1, task2, task3, task4]

    await asyncio.wait(task_list1)

    task_list = [count(counter), print_every_sec(counter), print_every_5sec(), print_every_10sec()]
    await asyncio.gather(*task_list)

asyncio.run(main())