import unittest
from ddt import ddt, file_data
from urllib import parse
import json

from driver_demo.common import requestclient
from driver_demo.common import readini
from driver_demo.common import jsonpath
from driver_demo.common import datahandler


@ddt
class TestFindbyid(unittest.TestCase):
    def setUp(self) -> None:
        self.url = readini.readIni(r'D:\Project\driver_demo\config\config.ini', 'URL', 'url')

    # @file_data(r'D:\Project\driver_demo\yaml\addNew.yaml')
    def test_findbyid(self):
        try:
            requests = datahandler.DataHandler.handle_data(r'D:\Project\driver_demo\yaml\findbyid.yaml')
            method = requests.get('method')
            url = self.url + requests.get('url')
            request = requests.get('request')
            request['data']['reqparams'] = json.dumps(request['data']['reqparams'])  # 将data字典中的数据reqparams进行json序列化
            # request['data'] = parse.urlencode(request.get('data'))  # 将data数据进行urlencode编码
            res = requestclient.httpClient(method, url, request)
            datahandler.DataHandler.writecache('servicetype', jsonpath.getJsonPath(res.text, "servicetype"))
            datahandler.DataHandler.writecache('kuaidicom', jsonpath.getJsonPath(res.text, "kuaidicomEn"))
            print(f'res:{res.text}')
        except Exception as e:
            raise e

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
