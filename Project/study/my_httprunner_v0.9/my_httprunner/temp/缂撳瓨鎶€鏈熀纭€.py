str1 = 'hello world'
print(f'str1: {str1}')

str2 = 'hello %s' % ('world')
print(f'str2: {str2}')

# java和python 模板替换参数的语法类型，模板语法类似
str3 = 'hello {world}，{name}'.format_map({'world': 'world 666', 'name': '高级测试'})  # format 可以实现 format_map功能
print(f'str3: {str3}')

# 正则表达式  在字符串里面找到符合格式的内容，如果涉及替换
# 一般项目中不用，面试题会考
import re

str4 = 'hello {world} {name}'
# str4 = 'hello $world $name'
# 用正则表达式提取 {world} {name}
re_pattern = '\{.{1,}\}'  # 获取的是 {world}  {name}
ret = re.findall(re_pattern, str4)
print(f'ret: {ret}')
# 再进行正则替换{world} {name} 进行替换

# --------
# 模板语法的定义和替换 python有内置模板替换的模块
from string import Template

# 第一个参数，放入原字符串（待替换的字符串），safe_substitute 放字典，这个功能类似format_map
# Template可以自定义模板语法
str5 = 'hello $world $name'
res = Template(str5).safe_substitute({'world': 'world 666', 'name': '模板替换测试'})
print(f'res: {res}')
