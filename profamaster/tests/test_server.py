from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

from ..web import start_server


class ProfamasterTestCase(AioHTTPTestCase):

    async def get_application(self):

        app = await start_server()
        return app

    # the unittest_run_loop decorator can be used in tandem with
    # the AioHTTPTestCase to simplify running
    # tests that are asynchronous
    @unittest_run_loop
    async def test_example(self):
        resp = await self.client.request("GET", "/")
        assert resp.status == 200
        text = await resp.text()
        assert "Hello, Anonymous" in text

    # a vanilla example
    def test_example_vanilla(self):
        async def test_get_route():
            url = "/"
            resp = await self.client.request("GET", url)
            assert resp.status == 200
            text = await resp.text()
            assert "Hello, Anonymous" in text

        self.loop.run_until_complete(test_get_route())
