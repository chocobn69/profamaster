from aiohttp import web
import logging

from profamaster.orders import (
    add_orders_in_queue,
)

logger = logging.getLogger(__name__)


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    try:
        await add_orders_in_queue(name)
    except Exception as e:
        logger.exception(e, exc_info=True)
    return web.Response(text=text)


# aiohttp server
async def start_server():
    logger.info('aiohttp server starting')
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    return app
