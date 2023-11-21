import asyncio
import httpx

async def dowload(current):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail'

    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        if result.status_code == 200:
            my_res = result.json()
            print_info(my_res['drinks'], current)
        else:
            print(result.status_code)
        print(f'Результат № {current}')


def print_info(info, current):
    #print(f"Имя {info["first_name"]}, Фамилия {info["last_name"]}, E-mail: {info["email"]}")
    print(info[current]['strDrink'])


async def main():
    users_count = int(input('Сколько?'))

    current = 0
    task_list = []
    while current < users_count:

        task = asyncio.create_task(dowload(current))
        task_list.append(task)
        current+=1
    await asyncio.gather(*task_list)
    print('Done')

asyncio.run(main())