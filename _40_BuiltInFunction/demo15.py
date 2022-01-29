# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 divmod() 函数
描述：
    函数接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)
    在 python 3.x 版本该函数不支持复数
语法：
    divmod(a, b)
    参数：
        a: 数字，非复数
        b: 数字，非复数
        1、如果参数 a 与 参数 b 都是整数，函数返回的结果相当于 (a // b, a % b)
        2、如果其中一个参数为浮点数时，函数返回的结果相当于 (q, a % b)，
           q 通常是 math.floor(a / b)，但也有可能是 1 ，比小，不过 q * b + a % b 的值会非常接近 a
        3、如果 a % b 的求余结果不为 0 ，则余数的正负符号跟参数 b 是一样的，
           若 b 是正数，余数为正数，若 b 为负数，余数也为负数，并且 0 <= abs(a % b) < abs(b)
'''
if __name__ == "__main__":
    print(divmod(7, 2))
    print(divmod(8, 2))
    print(divmod(8, -2))
    print(divmod(3, 1.3))
