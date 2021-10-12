# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典popitem()方法
                描述：
                    Python字典popitem()方法随机返回并删除字典中的最后一对键和值。
                    如果字典已经为空，却调用了此方法，就报出KeyError异常。
                语法：
                    popitem()
                    参数
                        无
                返回值：
                    返回一个键值对(key,value)形式，按照LIFO（Last In First Out后进先出法）
                    顺序规则，即最末尾的键值对。
"""
if __name__ == "__main__":
    site = {"name": "菜鸟教程", "alexa": 10000, "url": "www.runoob.com"}
    print("执行dict.popitem()方法前字典为：", site)
    pop_obj = site.popitem()
    print("执行dict.popitem()方法返回值为：", pop_obj)
    print("执行dict.popitem()方法后字典为：", site)
