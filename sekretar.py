import time
import asyncio

async def call():
    print('начался звонок')
    await asyncio.sleep(2)
    print('Звонок закончился')

async def prin_pos():
    print('Посетитель пришел')
    await asyncio.sleep(4)
    print('Посетитель пришел')


async def book():
    print('начало бронирования')
    await asyncio.sleep(3)
    print('Бронироание заверешно')

async def aeroticket():
    print('Выбор аивобилетов')
    await asyncio.sleep(2)
    print('Покупка авиабтлетов')


async def graficks():
    print('Начало работы с графиками ')
    await asyncio.sleep(2)
    print('Графики сделаны')


async def document():
    print('началось заполнение')
    await asyncio.sleep(5)
    print('заполнение завершено')




async def main():
    # task_call_aero = asyncio.create_task(call())
    # task_prin_pos = asyncio.create_task(prin_pos())


    print('9:00')
    await prin_pos()
    print('10:00')
    await asyncio.gather(aeroticket(), document())
    print('11:00')
    await call()
    print('12:00')
    await graficks()
    print('13:00')
    await asyncio.gather(aeroticket(), document())

asyncio.run(main())