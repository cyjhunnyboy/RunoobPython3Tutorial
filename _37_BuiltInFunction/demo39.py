# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 bytes 函数
描述：
    bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本
语法：
    class bytes([source[, encoding[, errors]]])
    参数：
        如果 source 为整数，则返回一个长度为 source 的初始化数组
        如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列
        如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数
        如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray
        如果没有输入任何参数，默认就是初始化数组为0个元素
返回值：
    返回一个新的 bytes 对象
'''
if __name__ == "__main__":
    byte_1 = bytes([1, 2, 3, 4])
    print(byte_1)
    print(type(byte_1))

    byte_2 = bytes('hello', 'ascii')
    print(byte_2)
    print(type(byte_2))
