from aiohttp import web
import logging
import json

from profamaster.orders import (
    add_orders_in_queue,
)

logger = logging.getLogger(__name__)

ERRORS = {
    'unknown pane': {
        'status': 'error',
        'error_code': 101,
        'message': 'unknown pane',
    },
    'unknown action': {
        'status': 'error',
        'error_code': 102,
        'message': 'unknown action',
    },
}

PANE_LIST = [1, ]


async def handle_error(request, error, status):
    return web.Response(
        status=status,
        text=json.dumps(error)
    )


async def handle(request):
    return web.Response(text=json.dumps({'status': 'ok'}))


async def handle_action(request):
    pane = int(request.match_info.get('pane', None))
    action = request.match_info.get('action', None)

    if action not in ['up', 'stop', 'down']:
        return await handle_error(request,
                                  error=ERRORS['unknown action'],
                                  status=503)

    if pane not in PANE_LIST:
        return await handle_error(request,
                                  error=ERRORS['unknown pane'],
                                  status=503)

    # handle action
    try:
        await add_orders_in_queue(action)
    except Exception as e:
        logger.exception(e, exc_info=True)
    return web.Response(text=json.dumps({'status': 'ok'}))


# aiohttp server
async def start_server():
    logger.info('aiohttp server starting')
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.post('/action/{pane}/{action}', handle_action)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    return app
