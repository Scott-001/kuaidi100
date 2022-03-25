'''
pip install pyyamlpip install pyyaml
'''
from pprint import pprint
from string import Template

import jmespath

'''
dumps （正）序列化  ， 结构化的语言(字符串) 转成 代码里面的对象，一般是数组或字典  （存进内存）
loads 反序列化   ， 把代码里面的对象，转成结构化的语言(字符串)，可以是json, yaml

dump  序列化，和上面的序列化有什么不同，这个序列化是把字符串存进硬盘
load  反序列化，把硬盘里的（文件）字符串，转成 代码里面的对象（内存）

'''
import yaml


class DataHandler:

    @classmethod  # 项目里面尽量不要出现相对路径，相对路径坑比较大，初学者填不上
    def handle_yaml(cls, file_abs_path):  # shift + 回车键，快速换行
        with open(file_abs_path, 'r') as f:  # ai的插件
            yaml_data = yaml.safe_load(f)  # f指向的是文件对象
        return yaml_data

    @classmethod
    def handle_template(cls, source_data, cache_data):
        '''
        模板替换
        :param source_data: 原数据
        :param cache_data: 缓存数据
        :return: 替换后的原数据
        '''
        res = Template(str(source_data)).safe_substitute(cache_data)
        return eval(res)  # 响应的res是个字符串？

    @classmethod
    def cache_data(cls, obj, path, cache_obj_key, cache):
        '''
        :param obj: 响应结果
        :param path: jmespath路径
        '''
        data = jmespath.search(path, obj)  # json path 找不到 返回None 找到就返回对应的值
        # if data is not None:
        if data:  # 开发中比较好的写法
            cache.update({cache_obj_key: data})
        return cache

if __name__ == '__main__':
    # 格式快捷键 ctrl+alt+L
    # data = DataHandler.handle_yaml('/Users/dengjiajie/Desktop/my_git_v2/my_httprunner/data/test_demo.yaml')
    # pprint(data)
    obj = {
        "args": {
            "k1": "v1",
            "k2": "kkkkkk"
        },
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "httpbin.org",
            "User-Agent": "python-requests/2.26.0",
            "X-Amzn-Trace-Id": "Root=1-622c5605-7c33baed4b10c9de5ba3c759"
        },
        "origin": "113.87.182.184",
        "url": "http://httpbin.org/get?k1=v1&k2=kkkkkk"
    }
    cache_obj = dict()  # 定义一个空字典来存临时的变量，实现上下文关联
    DataHandler.cache_data(obj=obj, path='args.k2', cache_obj_key='k2', cache=cache_obj)
    print(cache_obj)  # {'k2': 'kkkkkk'}
