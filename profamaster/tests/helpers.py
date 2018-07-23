from aiohttp.test_utils import AioHTTPTestCase
from unittest.mock import patch, MagicMock


# we need to this before importing start_server
MockRPi = MagicMock()
modules = {
    "RPi": MockRPi,
    "RPi.GPIO": MockRPi.GPIO,
}
patcher = patch.dict("sys.modules", modules)
patcher.start()

from profamaster.orders import exec_orders_in_queue  # noqa


class BaseTestCase(AioHTTPTestCase):
    def setUp(self):
        super().setUp()
        self.loop.create_task(exec_orders_in_queue())

    def teardown(self):
        super().tearDown()
        patcher.stop()
