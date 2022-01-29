# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 移除字典点键值(key/value)对
    给定一个字典，然后计算它们所有数字值的和。
'''
if __name__ == "__main__":
    # 使用pop()移除
    test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

    # 输出原始的字典
    print("字典移除前：" + str(test_dict))

    # 使用pop移除 Zhihu
    removed_value = test_dict.pop("Zhihu")

    # 输出移除后的字典
    print("字典移除后：" + str(test_dict))

    print("移除的key对应的value为：" + str(removed_value))

    print("\r")

    # 使用pop()移除没有的key不会发生异常，我们可以自定义提示信息
    removed_value = test_dict.pop("Baidu", "没有该键(key)")

    # 输出移除后的字典
    print("字典移除后：" + str(test_dict))
    print("移除的值为：" + str(removed_value))
