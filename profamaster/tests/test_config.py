import unittest
import os

from profamaster.config import load_config 


class ConfigTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_load_config(self):
        # import config module and check config datas
        CONFIG = load_config(
            os.path.realpath(
                os.path.join('./',
                             'profamaster/tests/config.yaml')))

        self.assertEquals(1, CONFIG['registers_nb'])
        self.assertDictEqual(
            CONFIG['panes'],
            {
                1: {
                    'name': 'a room',
                    'exec_time': 700,
                    'gpio': {
                        'up': 1,
                        'down': 2,
                        'stop': 3,
                    },
                },
                2: {
                    'name': 'another room',
                    'exec_time': 800,
                    'gpio': {
                        'up': 4,
                        'down': 5,
                        'stop': 6,
                    },
                },
            }
        )
        self.assertDictEqual(
            CONFIG['web'],
            {
                'port': 8080,
                'host': 'localhost',
            }
        )
