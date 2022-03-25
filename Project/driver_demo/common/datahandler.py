from string import Template
import yaml
import json

from driver_demo.common import jsonpath


class DataHandler:
    # new_dict = dict()
    new_dict = dict()

    # 模板替换函数
    # @classmethod
    def handle_template(self, source_data, cache_data):
        return Template(str(source_data)).safe_substitute(cache_data)

    # 读取yaml文件数据
    @classmethod
    def readyaml(cls, file_path):
        with open(file_path, mode='rt', encoding='utf-8') as f:
                new_object = yaml.load(f)[0]
        return new_object

    # 写入缓存数据
    @classmethod
    def writecache(cls, key, value):
        data = dict()
        if key in data.items():
            data[key + '1'] = value
        data[key] = value
        DataHandler.new_dict.update(data)

    # @classmethod
    # def replace_data(cls, cache_dict, new_data_dict):
    #     for key, value in new_data_dict.items():
    #         if key in cache_dict:
    #             new_data_dict[key] = cache_dict[key]
    #         else:
    #             print("抱歉！缓存字典没有这个值！")
    #     return new_data_dict
    # 模板替换之后的返回字典
    @classmethod
    def handle_data(cls, file_path):
        datahandle = DataHandler()
        new_data_dict = datahandle.readyaml(file_path)
        object_data = datahandle.handle_template(new_data_dict, datahandle.new_dict)
        return eval(object_data)


if __name__ == '__main__':
    datahandle = DataHandler()
    # print(type(datahandle.new_dict))
    new_data_dict = datahandle.readyaml(r'D:\Project\driver_demo\yaml\addNewBatch.yaml')
    # print(datahandle.replace_data(datahandle.new_dict, new_data_dict))
    # print(datahandle.handle_template(new_data_dict, datahandle.new_dict))
    # print(new_data_dict, type(new_data_dict))
    # print(datahandle.handle_data())
    print(new_data_dict)

