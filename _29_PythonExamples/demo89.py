# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 对字符串切片及翻转
    给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。
'''


def rotate(input, d):
    """给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。"""

    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))


if __name__ == "__main__":
    input = "Runoob"
    # 截取两个字符
    d = 2
    rotate(input, d)
