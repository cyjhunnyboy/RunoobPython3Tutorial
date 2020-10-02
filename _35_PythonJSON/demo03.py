# -*- coding: UTF-8 -*-
# author: chenyongjun
import json

data = {
    "no": 1,
    "name": "Runoob",
    "url": "http://www.runoob.com"
}

# 写入 JSON 数据
with open("data/data.json", "w") as f:
    json.dump(data, f)

# 读取JSON数据
with open("data/data.json", "r") as f:
    data = json.load(f)
    print(data)
    for key, value in data.items():
        print("key = ", key, "value = ", value)
