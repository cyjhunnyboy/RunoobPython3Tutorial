# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    10、dictionary 中的解析
'''
if __name__ == "__main__":
    params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
    print(params)
    print(params.keys())
    print(params.values())
    print(params.items())

    print([k for k, v in params.items()])
    print([v for k, v in params.items()])
    print(["%s=%s" % (k, v) for k, v in params.items()])
