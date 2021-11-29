# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 编程第一步
        Fibonacci series: 斐波纳契数列，两个元素的总和确定了下一个数
"""
if __name__ == "__main__":
    # Fibonacci series: 斐波纳契数列
    # 两个元素的总和确定了下一个数
    # 第一行包含了一个复合赋值：变量a和b同时得到新值0和1。
    # 最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。
    # 右边表达式的执行顺序是从左往右的
    a, b = 0, 1
    while b < 10:
        print(b)
        a, b = b, a + b
