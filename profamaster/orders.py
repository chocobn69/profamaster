import asyncio
import logging

from profamaster.config import (
    queue,
    TIME_BETEWEEN_EXEC,
)

logger = logging.getLogger(__name__)


def pane_movement(p_number, way, percent_move=1.0):
    """ move up/down pane number p_number to x percent """
    if way not in ['up', 'down']:
        raise AttributeError('way has to be either up or down')


async def exec_orders_in_queue():
    """ read fifo queue and execute orders sequentialy """
    while True:
        order = await queue.get()
        if order is not None:
            logger.debug('exec orders %s', order)
            await asyncio.sleep(TIME_BETEWEEN_EXEC)
        queue.task_done()


async def add_orders_in_queue(order):
    """ add order in async Queue (fifo) """
    logger.debug('add_orders_in_queue %s', order)
    await queue.put(order)
