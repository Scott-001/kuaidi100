import os
import logging
import pytest
from loguru import logger
# 从文件或者数据库 读取用例
from utils.data_driver_handler import DataDriverHandler
from utils.data_handler import DataHandler

CAST_LIST = DataHandler.handle_yaml('/Users/dengjiajie/Desktop/my_git_v2/my_httprunner/data/test_demo.yaml')
CAST_LIST = CAST_LIST.get('test_case')

# 把用例放进ddt里面执行
class TestDemo:

    @pytest.mark.parametrize('test_case', CAST_LIST)
    def test_demo(self, test_case):
        print(f'test_case:{test_case} ')
        data_driver = DataDriverHandler(test_case).data_run()

        # print(f'test_case:{test_case}')
        # requests_handler = RequestHandler()
        # requests_handler.send_http_v1()

if __name__ == '__main__':
    pytest.main(['-s', '-v', f'{os.path.abspath(__file__)}',
                 '--capture=sys',
                 '--log-level=INFO',
                 f'--html=./report.html'
                 ])
