# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    7、使用join链接list成为字符串
        join只能用于元素是字符串的list; 它不进行任何的类型强制转换。
        连接一个存在一个或多个非字符串元素的list将引发一个异常
'''
if __name__ == "__main__":
    params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
    params_list = ["%s=%s" % (k, v) for k, v in params.items()]
    print(params)
    print(params_list)

    params_list = ";".join(["%s=%s" % (k, v) for k, v in params.items()])
    print(params_list)
