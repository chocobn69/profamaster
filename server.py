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


queue = asyncio.Queue()


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
        queue.task_done()

async def add_orders_in_queue(order):
    """ add order in async Queue (fifo) """
    logger.debug('add_orders_in_queue %s', order)
    await queue.put(order)

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    logger.debug(name)
    try:
        await add_orders_in_queue(name)
    except Exception as e:
        logger.exception(e, exc_info=True)
    return web.Response(text=text)

# aiohttp server
logger.debug('aiohttp server starting')
app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])
web.run_app(app, access_log=logger)

# loop exec
logger.debug('loop exec')
loop = asyncio.get_event_loop()
loop.create_task(exec_orders_in_queue())
loop.run_forever()