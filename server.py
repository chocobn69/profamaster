import logging
from aiohttp import web

logger = logging.getLogger(__name__)

TIME_BETEWEEN_EXEC = 500


def pane_movement(p_number, way, percent_move=1.0):
    """ move up/down pane number p_number to x percent """
    if way is not in ['up', 'down']:
        raise AttributeError('way has to be either up or down')


async def exec_orders_queue():
    """ read fifo queue and execute orders sequentialy """
    pass

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)
