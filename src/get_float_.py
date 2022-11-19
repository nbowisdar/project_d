import asyncio
import json
from fake_useragent import UserAgent
import aiohttp
from loguru import logger
from schema.items_schema import ForGetProfileSchema, ForGetFloatSchema, \
    ItemsForGetFloatSchema
from src.urls import BASE_FLOAT_URL
from time import perf_counter

count = 0
errors = 0

async def get_float(item: ForGetFloatSchema) -> dict | None:
    global errors
    global count
    count += 1
    print(f'Loading... {count / 9} / 100 %')
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': UserAgent().random}
        async with session.get(BASE_FLOAT_URL+item.in_game, headers=headers) as resp:
            try:
                resp_j = await resp.text()
                info = json.loads(resp_j)['iteminfo']
                return ForGetProfileSchema(
                    link_dm=item.link_dm,
                    name=info['item_name'],
                    float_value=info['floatvalue'],
                    paint_seed=info['paintseed']
                ).dict()
            except Exception as err:
                logger.error(err)
                errors += 1
                return None


async def pars_all(data: ItemsForGetFloatSchema, save=False) -> list[dict]:
    tasks = []
    for item in data.items:
        tasks.append(get_float(item))
    logger.info('all tasks generated')

    items = []
    for task in tasks:
        resp = await task
        if resp:
            items.append(resp)

    logger.info('Collected all!')
    if save:
        with open('output/with_float.json', 'w', encoding='utf-8') as file:
            json.dump(items, file, indent=2)

    return items


def start_parsing(*args, **kwargs):
    s = asyncio.run(pars_all(*args, **kwargs))
    #logger.info(s)


if __name__ == '__main__':
    with open('output/items.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        items = ItemsForGetFloatSchema(items=data['items'])

    start = perf_counter()
    start_parsing(items, save=True)
    finish = perf_counter() - start
    logger.info(f'Took seconds - {finish}')
    logger.error(f'Amount of error - {errors}')
