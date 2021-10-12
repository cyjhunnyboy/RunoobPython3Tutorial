# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典update()方法
                描述：
                    Python字典update()函数把字典参数dict2的key/value(键/值)对更新到字典dict里。
                语法：
                    dict.update(dict2)
                    参数
                        dict2 -- 添加到指定字典dict里的字典。
                返回值
                    该方法没有任何返回值。
"""
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}
    dict_b = {"Sex": "female"}

    dict_a.update(dict_b)
    print("更新的字典dict_b为：", dict_b)
    print("被更新后字典dict_a为：", dict_a)
