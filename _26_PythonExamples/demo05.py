# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 平方根
    通过用户输入一个数字，并计算这个数字的平方根
    计算实数和复数平方根，需导入复数数学模块import cmath
    cmath(complex math)模块的sqrt()方法来计算平方根
'''
import cmath

if __name__ == "__main__":
    # 正数、负数和复数
    num = int(input("请输入一个数字："))
    num_sqrt = cmath.sqrt(num)
    print("{0}的平方根为：{1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))
