from aiohttp.test_utils import unittest_run_loop
from unittest.mock import patch
import json

from profamaster.tests.helpers import BaseTestCase
from profamaster.web import start_server


class ProfamasterTestCase(BaseTestCase):

    async def get_application(self):
        """ get app from web.start_server """
        app = await start_server()
        return app

    async def _test_call(self,
                         method='GET',
                         url='/',
                         asserted_status=200,
                         asserted_response={}):
        resp = await self.client.request(method, url)
        self.assertEqual(resp.status, asserted_status)
        text = await resp.text()
        if asserted_response:
            self.assertDictEqual(asserted_response,
                                 json.loads(text))

    @unittest_run_loop
    async def test_root(self):
        await self._test_call('GET', '/', 200, {'status': 'ok'})

        # try 404
        await self._test_call('GET', '/toto', 404, None)

    @patch('profamaster.orders.add_orders_in_queue')
    @unittest_run_loop
    async def test_actions(self, mock_add_orders_in_queue):

        # first, try legit actions
        # test action up on pane 1
        await self._test_call('POST', '/action/1/up', 200, {'status': 'ok'})
        mock_add_orders_in_queue.assert_called_once()
        mock_add_orders_in_queue.reset_mock()

        # test action stop on pane 1
        await self._test_call('POST', '/action/1/stop', 200, {'status': 'ok'})
        mock_add_orders_in_queue.assert_called_once()
        mock_add_orders_in_queue.reset_mock()

        # test action down on pane 1
        await self._test_call('POST', '/action/1/down', 200, {'status': 'ok'})
        mock_add_orders_in_queue.assert_called_once()
        mock_add_orders_in_queue.reset_mock()

        # try with not POST method
        await self._test_call('GET', '/action/1/up', 405, None)
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()

        # now try with unknown pane
        # test action up on pane 9
        await self._test_call('POST', '/action/9/up', 503,
                              {
                                  'status': 'error',
                                  'error_code': 101,
                                  'message': 'unknown pane',
                              })
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()

        # test action stop on pane 9
        await self._test_call('POST', '/action/9/stop', 503,
                              {
                                  'status': 'error',
                                  'error_code': 101,
                                  'message': 'unknown pane',
                              })
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()

        # test action down on pane 9
        await self._test_call('POST', '/action/9/down', 503,
                              {
                                  'status': 'error',
                                  'error_code': 101,
                                  'message': 'unknown pane',
                              })
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()

        # now try with non legit actions
        await self._test_call('POST', '/action/1/stale', 503,
                              {
                                  'status': 'error',
                                  'error_code': 102,
                                  'message': 'unknown action',
                              })
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()

        await self._test_call('POST', '/action/1/948759348759', 503,
                              {
                                  'status': 'error',
                                  'error_code': 102,
                                  'message': 'unknown action',
                              })
        mock_add_orders_in_queue.assert_not_called()
        mock_add_orders_in_queue.reset_mock()
