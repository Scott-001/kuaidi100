import unittest
from ddt import ddt, file_data
from urllib import parse
import json

from driver_demo.common import requestclient
from driver_demo.common import readini
from driver_demo.common import jsonpath
from driver_demo.common import datahandler


@ddt
class TestElecorderInfo(unittest.TestCase):
    def setUp(self) -> None:
        self.url = readini.readIni(r'D:\Project\driver_demo\config\config.ini', 'URL', 'url')

    # @file_data(r'D:\Project\driver_demo\yaml\addNew.yaml')
    def test_elecorderinfo(self):
        try:
            requests = datahandler.DataHandler.handle_data(r'D:\Project\driver_demo\yaml\elecorderinfo.yaml')
            method = requests.get('method')
            url = self.url + requests.get('url')
            request = requests.get('request')
            res = requestclient.httpClient(method, url, request)
            print(f'res:{res.text}')
        except Exception as e:
            raise e

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
