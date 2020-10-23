# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
旧式字符串格式化
    %操作符也可以实现字符串格式化。
    它将左边的参数作为类似sprintf()式的格式化字符串，而将右边的代入，然后返回格式化后的字符串。

    因为str.format()是比较新的函数，大多数的Python代码仍然使用%操作符。
    但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用str.format().
'''
import math

if __name__ == "__main__":
    print("常量PI的值近似为：%5.3f。" % math.pi)
