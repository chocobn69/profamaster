import unittest


class ConfigTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_load_config(self):
        # import config mdule and check config datas
        from profamaster.config import CONFIG

        self.assertEquals('profalux', CONFIG['pane_module'])
        self.assertDictEqual(
            CONFIG['panes'],
            {
                1: {
                    'name': 'a room',
                    'exec_time': 700,
                },
                2: {
                    'name': 'another room',
                    'exec_time': 800,
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
