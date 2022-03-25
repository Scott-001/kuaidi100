from utils.client import Client
from utils.data_handler import DataHandler


class DataDriverHandler:

    def __init__(self, test_case):
        # 接收用例的描述——yaml用例描述
        self.case_name = test_case.get('case_name')
        self.interface_name = test_case.get('interface_name')
        self.request = test_case.get('request')
        self.extract = test_case.get('extract')
        '''
        self.extract = { 'k2': 'json.args.k2','k3': 'json.args.k3' }
        '''

    def data_run(self):
        '''
        data_run 实际上是一个请求流程，这个流程由不同方法组成
        :return:
        '''
        # 1、发送http请求
        client = Client()
        resp = client.send_http_v1(self.request)

        # 2、断言
        # 后面讲

        # 3、提取参数
        if self.extract:
            print(f'为缓存前 DataHandler.cache : {DataHandler.cache}')
            DataHandler.cache_data(resp, self.extract)
            print(f'缓存后 DataHandler.cache : {DataHandler.cache}')
