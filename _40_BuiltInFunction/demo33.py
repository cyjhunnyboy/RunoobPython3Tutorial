# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python bytearray() 函数
描述：
    bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
语法：
    class bytearray([source[, encoding[, errors]]])
    参数：
        如果 source 为整数，则返回一个长度为 source 的初始化数组
        如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列
        如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数
        如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray
        如果没有输入任何参数，默认就是初始化数组为0个元素
返回值：
    返回新字节数组
'''
if __name__ == "__main__":
    print(bytearray())
    print(bytearray([1, 2, 3]))
    print(bytearray("runoob", "utf-8"))
