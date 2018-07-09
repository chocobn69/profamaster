'''
profamaster config module
'''

import asyncio
import logging.config


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
        'root': {
            'handlers': ['console']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', ]
    },
})

queue = asyncio.Queue()

TIME_BETEWEEN_EXEC = 0.7
