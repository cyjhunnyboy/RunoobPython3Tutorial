# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 移除字符串中的指定位置字符
    给定一个字符串，然后移除指定位置的字符
'''


def delete(test_str, index):
    """给定一个字符串，然后移除指定位置的字符"""

    # 移除第index个字符
    new_str = ""

    for i in range(0, len(test_str)):
        if i != index - 1:
            new_str = new_str + test_str[i]

    return new_str


if __name__ == "__main__":
    test_str = "Runoob"

    # 输出原始字符串
    print("原始字符串为：" + test_str)

    # 移除第三个字符n
    print("字符串移除后为：" + delete(test_str, 3))
