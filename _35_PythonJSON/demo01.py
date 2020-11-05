# -*- coding: UTF-8 -*-
# author: chenyongjun
import json

# Python 字典类型转换为 JSON 对象
data = {
    "no": 1,
    "name": "Runoob",
    "url": "http://www.runoob.com"
}

json_str = json.dumps(data)
print("Python原始数据：", repr(data))
print("JSON对象：", json_str)
