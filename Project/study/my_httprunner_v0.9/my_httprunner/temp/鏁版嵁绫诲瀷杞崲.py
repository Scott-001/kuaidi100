'''
字典转字符串
'''

dict1 = {'method': 'GET',
         'params': {'k1': 'v1', 'k2': '$k2'},
         'url': 'http://httpbin.org/get'}


print(f'type dict1: {type(dict1)}')

dict1_to_str = str(dict1)
print(dict1_to_str)
print(f'type dict1_to_str: {type(dict1_to_str)}')

'''
字符串如何转字典
eval: 相当于'反射'，eval('字符串')，会映射进pyton的数据类型
字符串格式要符合python数据类型的表达
js python 这些脚本语言才有？ eval
'''


