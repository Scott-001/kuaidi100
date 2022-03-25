import jsonpath
import json


def getJsonPath(json_data, data):
    try:
        txt = json.loads(json_data)
        value = jsonpath.jsonpath(txt, '$..{0}'.format(data))
        if value:
            if len(value) == 1:
                return value[0]
            return value
    except Exception as e:
        print(f'数据提取失败:{e}')


