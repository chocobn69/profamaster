import asyncio
import logging

from profamaster.web import start_server
from profamaster.orders import exec_orders_in_queue

logger = logging.getLogger(__name__)


# loop exec
if __name__ == '__main__':
    logger.debug('loop exec')
    loop = asyncio.get_event_loop()
    loop.create_task(start_server())
    loop.create_task(exec_orders_in_queue())
    loop.run_forever()
