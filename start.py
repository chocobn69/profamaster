#!/usr/bin/env python

import asyncio
import logging
import functools
import signal

from profamaster.web import start_server
from profamaster.orders import exec_orders_in_queue
from profamaster.config import CONFIG
from profamaster.shiftpi.shiftpi import (
    LOW,
    startupMode,
    shiftRegisters
)

logger = logging.getLogger(__name__)


def ask_exit(signame):
    logger.info("got signal %s: exit" % signame)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, signame),
                                functools.partial(ask_exit, signame))
    try:
        logger.debug('start server')
        shiftRegisters(CONFIG['registers_nb'])
        startupMode(LOW)
        loop.create_task(start_server())
        loop.create_task(exec_orders_in_queue())
        loop.run_forever()
    except KeyboardInterrupt:
        logger.debug('Ctrl+C pressed, stopping')
