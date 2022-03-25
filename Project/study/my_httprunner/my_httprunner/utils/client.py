from pprint import pprint

import requests

from utils.data_handler import DataHandler


class RequestHandler:

    def send_http_v1(self, request_data):
        resp = requests.request(**request_data)
        # pprint(resp.json())  # 快速引包，alt+回车
        print(resp.text)
        # return resp

    # 请求的类型：HTTP1.1 HTTP2.0  grpc PD写， duboo

    def run_datas(self, test_case):
        test_case = test_case['test_case']
        for case in test_case:
            print(f'case_name: {case["case_name"]}')
            print(f'interface_name: {case["interface_name"]}')
            request_data = case['request']
            request_data = DataHandler.handle_template(request_data, {'k2': 'kkkkkk'})
            self.send_http_v1(request_data)
            print(f'\n'
                  f'分割线---\n'
                  f'\n')


if __name__ == '__main__':
    requests_data = {'test_case': [{'case_name': '测试GET请求发送成功',
                                    'interface_name': 'GET请求的测试路由',
                                    'request': {'method': 'GET',
                                                'params': {'k1': 'v1', 'k2': '$k2'},
                                                'url': 'http://httpbin.org/get'}},
                                   {'case_name': '测试POST请求发送成功',
                                    'interface_name': 'POST请求的测试路由',
                                    'request': {'data': {'k1': 'v1', 'k2': 'v2'},
                                                'method': 'POST',
                                                'url': 'http://httpbin.org/post'}}]}
    requests_handler = RequestHandler()
    requests_handler.run_datas(requests_data)

# json 提取， jmespath
# jsonpath python维护不好，没有专门维护
# jsonpath-rw 语法类是jmespath ，没有转维护
# jmespath 新起之秀，有专门的维护和官网  java也有，你们看jmeter也有这个语法，5.0以上一定有


    # requests_handler.send_http_v1(requests_data['test_case'][0]['request'])
    # requests_handler.send_http_v1({'method': 'GET',
    #                                             'params': {'k1': 'v1', 'k2': 'v2'},
    #                                             'url': 'http://httpbin.org/get'})
