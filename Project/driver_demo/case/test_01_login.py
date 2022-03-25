import unittest
from ddt import ddt, file_data
from urllib import parse
import json

from driver_demo.common import requestclient
from driver_demo.common import readini
from driver_demo.common import jsonpath
from driver_demo.common import datahandler


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url = readini.readIni(r'D:\Project\driver_demo\config\config.ini', 'URL', 'url')

    @file_data(r'D:\Project\driver_demo\yaml\login.yaml')
    def test_login(self, method, url, request, **kwargs):
        try:
            url = self.url + url
            request['data']['reqparams'] = json.dumps(request['data']['reqparams'])  # 将data字典中的数据reqparams进行json序列化
            request['data'] = parse.urlencode(request.get('data'))  # 将data数据进行urlencode编码
            res = requestclient.httpClient(method, url, request)
            # 将接口返回信息写入缓存
            # token
            datahandler.DataHandler.writecache('token', jsonpath.getJsonPath(res.text, "token"))
            # courierid
            datahandler.DataHandler.writecache('courierid', jsonpath.getJsonPath(res.text, "courierid"))
            # userid
            datahandler.DataHandler.writecache('userid', jsonpath.getJsonPath(res.text, "userid"))
            # optor
            datahandler.DataHandler.writecache('optor', jsonpath.getJsonPath(res.text, "optor"))

            print(f'res:{res.text}')
        except Exception as e:
            raise e

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
