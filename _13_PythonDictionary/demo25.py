# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典pop()方法
                描述：
                    Python字典pop()方法删除字典给定键key所对应的值，返回值为被删除的值。
                    key值必须给出。否则，返回default值。
                语法：
                    pop(key[,default])
                    参数
                        key: 要删除的键值
                        default: 如果没有key，返回default值
                返回值
                    返回被删除的值
"""
if __name__ == "__main__":
    site = {"name": "菜鸟教程", "alexa": 10000, "url": "www.runoob.com"}
    print("执行dict.pop(\"name\")方法前字典为：", site)

    # 删除字典给定键key所对应的值，返回值为被删除的值
    pop_obj = site.pop("name")
    print("被删除键[\"name\"]对应的值为：", pop_obj)
    print("执行dict.pop(\"name\")方法后字典为：", site)
