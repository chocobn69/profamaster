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


class BaseTestCase(AioHTTPTestCase):

    def teardown(self):
        patcher.stop()
