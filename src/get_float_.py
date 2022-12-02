import asyncio
import json
import time

from fake_useragent import UserAgent
import aiohttp
from loguru import logger
from schema.new_schema import ForGetProfileSchema, ForGetFloatSchema
from src.urls import BASE_FLOAT_URL

count = 0
errors = 0
all_items_amount = 0


async def get_float_one_item(item: ForGetFloatSchema) -> ForGetProfileSchema | None:
    global errors
    global count
    count += 1
    print(f'Loading... {count} / {all_items_amount} ')
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': UserAgent().random}
        url = BASE_FLOAT_URL+item.in_game
        async with session.get(url, headers=headers) as resp:
            try:
                resp_j = await resp.text()
                info = json.loads(resp_j)['iteminfo']
                return ForGetProfileSchema(
                    link_dm=item.link_dm,
                    name=item.item_name,
                    float_value=info['floatvalue'],
                    paint_seed=info['paintseed']
                )
            except Exception as err:
                logger.error(err)
                logger.error(url)
                errors += 1
                return None


async def pars_all(items: list[ForGetFloatSchema]) -> list[ForGetProfileSchema]:
    tasks = []
    global all_items_amount
    all_items_amount = len(items)
    for item in items:
        # time.sleep(10)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        tasks.append(get_float_one_item(item))
    logger.info('all tasks generated')

    items_new = []
    for task in tasks:
        resp = await task
        if resp:
            items_new.append(resp)

    logger.info('Have got float!')
    return items_new


def get_float(items: list[ForGetFloatSchema]) -> list[ForGetProfileSchema]:
    while True:
        try:
            return asyncio.run(pars_all(items))
        except Exception as err:
            logger.error(err)
            logger.info('continue')


# if __name__ == '__main__':
#     with open('output/items.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         items = ItemsForGetFloatSchema(items=data['items'])
#
#     start = perf_counter()
#     start_parsing(items, save=True)
#     finish = perf_counter() - start
#     logger.info(f'Took seconds - {finish}')
#     logger.error(f'Amount of error - {errors}')
