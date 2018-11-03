'''
profamaster config module
'''

import asyncio
import os
import logging.config
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_config(config_path):
    ''' load config file filname '''
    with open(config_path, 'r') as stream:
        return load(stream, Loader=Loader)


CONFIG_FILE = './config.yaml'


def lazy_load_config():
    return load_config(os.path.realpath(CONFIG_FILE))


CONFIG = lazy_load_config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s '
                      '%(levelname)-8s %(processName)-10s %(message)s'
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
        'aiohttp.access': {
            'handlers': ['console']
        },
        'aiohttp.server': {
            'handlers': ['console']
        },
        'root': {
            'handlers': ['console']
        }
    },
    'profamaster.orders': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
    'shiftpi': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
    'aiohttp.access': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
    'aiohttp.server': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
})

queue = asyncio.Queue()

TIME_BETWEEN_EXEC = 0.2
