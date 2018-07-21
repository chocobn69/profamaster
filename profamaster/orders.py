import asyncio
import logging

from profamaster.shiftpi.shiftpi import (
    HIGH,
    LOW,
    digitalWrite,
    startupMode,
    delay,
    shiftRegisters
)

from profamaster.config import (
    queue,
    CONFIG,
    TIME_BETWEEN_EXEC,
)

logger = logging.getLogger(__name__)

shiftRegisters(1)
startupMode(LOW)


def pane_action(pane, action):
    """ exec pane action """
    if action not in ['up', 'stop', 'down']:
        raise AttributeError('action has to be either up down or stop')

    # exec action...
    pass
    digitalWrite(CONFIG[pane]['gpio'][action], HIGH)
    delay(CONFIG[pane]['exec_time'])
    digitalWrite(CONFIG[pane]['gpio'][action], LOW)


async def exec_orders_in_queue():
    """ read fifo queue and execute orders sequentialy """
    logger.info('start exec_orders_in_queue loop')
    while True:
        order = await queue.get()
        if order is not None:
            logger.debug('exec orders %s', order)
            pane = order['pane']
            action = order['action']
            pane_action(pane, action)
            await asyncio.sleep(TIME_BETWEEN_EXEC)
        queue.task_done()


async def add_orders_in_queue(order):
    """ add order in async Queue (fifo) """
    logger.debug('add_orders_in_queue %s', order)
    await queue.put(order)
