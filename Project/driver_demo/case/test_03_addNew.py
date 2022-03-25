import unittest
from ddt import ddt, file_data
from urllib import parse
import json

from driver_demo.common import requestclient
from driver_demo.common import readini
from driver_demo.common import jsonpath
from driver_demo.common import datahandler


@ddt
class TestAddNew(unittest.TestCase):
    def setUp(self) -> None:
        self.url = readini.readIni(r'D:\Project\driver_demo\config\config.ini', 'URL', 'url')

    # @file_data(r'D:\Project\driver_demo\yaml\addNewbatch.yaml')
    def test_addNew(self):
        try:
            requests = datahandler.DataHandler.handle_data(r'D:\Project\driver_demo\yaml\addNew.yaml')
            # print(f'requests:{requests}')
            method = requests.get('method')
            url = self.url + requests.get('url')
            request = requests.get('request')
            request['data']['reqparams'] = json.dumps(request['data']['reqparams'])  # 将data字典中的数据reqparams进行json序列化
            request['data'] = parse.urlencode(request.get('data'))  # 将data数据进行urlencode编码
            res = requestclient.httpClient(method, url, request)
            # 将订单id写入缓存
            datahandler.DataHandler.writecache('expid', jsonpath.getJsonPath(res.text, "expid"))
            print(f'res:{res.text}')
        except Exception as e:
            raise e

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
