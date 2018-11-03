import logging
import time
import asyncio

from profamaster.shiftpi.shiftpi import (
    HIGH,
    LOW,
    digitalWrite,
    delay,
)

from profamaster.config import (
    CONFIG,
    TIME_BETWEEN_EXEC,
    queue,
)

logger = logging.getLogger(__name__)


def pane_action(pane, action):
    """ exec pane action """
    if action not in ['up', 'stop', 'down']:
        raise AttributeError('action has to be either up down or stop')
    logger.debug('start pane %s action %s', pane, action)

    # exec action...
    digitalWrite(CONFIG()['panes'][int(pane)]['gpio'][action], HIGH)
    delay(CONFIG()['panes'][int(pane)]['exec_time'])
    digitalWrite(CONFIG()['panes'][int(pane)]['gpio'][action], LOW)

    logger.debug('end pane %s action %s', pane, action)


async def exec_orders_in_queue():
    """ read fifo queue and execute orders sequentialy """
    logger.info('start exec_orders_in_queue loop')
    while True:
        order = await queue.get()
        if order is not None:
            pane = order['pane']
            action = order['action']
            pane_action(pane, action)
            asyncio.sleep(TIME_BETWEEN_EXEC)
        queue.task_done()


async def add_orders_in_queue(order):
    """ add order in async Queue (fifo) """
    logger.debug('add_orders_in_queue %s', order)
    await queue.put(order)
