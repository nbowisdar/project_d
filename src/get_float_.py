import asyncio
import json
from fake_useragent import UserAgent
import aiohttp
from loguru import logger
from schema.items_schema import ForGetProfileSchema, ForGetFloatSchema

BASE_URL = 'https://api.csgofloat.com/?url='

count = 0
async def get_float(item: ForGetFloatSchema) -> ForGetProfileSchema | None:
    global count
    count+=1
    print(count)
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': UserAgent().random}
        async with session.get(BASE_URL+item.in_game, headers=headers) as resp:
            try:
                resp_j = await resp.text()
                info = json.loads(resp_j)['iteminfo']
                return ForGetProfileSchema(
                    link_dm=item.link_dm,
                    name=info['item_name'],
                    float_value=info['floatvalue'],
                    paint_seed=info['paintseed']
                )
            except Exception as err:
                logger.error(err)
                return None


async def pars_all(data: list[ForGetFloatSchema], save=False) -> list[ForGetProfileSchema]:
    tasks = []
    for item in data:
        tasks.append(get_float(item))
    logger.info('all tasks created')
    items = []
    for task in tasks:
        resp = await task
        items.append(resp.dict())

    logger.info('Collected all!')
    if save:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(items, file)
    return items


def start_parsing(*args, **kwargs):
    s = asyncio.run(pars_all(*args, **kwargs))
    logger.info(s)


# if __name__ == '__main__':
#     pars_all([ForGetFloatSchema(
#         in_game='https://api.csgofloat.com/?url=steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561199016162011A27196423987D12252291978405198829',
#         link_dm='http://hello'
#     )])