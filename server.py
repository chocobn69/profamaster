import logging.config
import logging
from aiohttp import web
import asyncio


logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
})

logger = logging.getLogger(__name__)

TIME_BETEWEEN_EXEC = 500


def pane_movement(p_number, way, percent_move=1.0):
    """ move up/down pane number p_number to x percent """
    if way not in ['up', 'down']:
        raise AttributeError('way has to be either up or down')


async def exec_orders_in_queue():
    """ read fifo queue and execute orders sequentialy """
    while True:
        order = await queue.get()
        if order is not None:
            logger.debug(order)

async def add_orders_in_queue(order):
    """ add order in async Queue (fifo) """
    logger.debug('add_orders_in_queue %s', order)
    await queue.put(order)

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    logger.debug(name)
    await add_orders_in_queue(name)
    return web.Response(text=text)

def run():

    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    web.run_app(app, access_log=logger)
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)


if __name__ == "__main__":
    run()
