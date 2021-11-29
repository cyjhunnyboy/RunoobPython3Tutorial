# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 编程第一步
        Fibonacci series: 斐波纳契数列，两个元素的总和确定了下一个数
"""
if __name__ == "__main__":
    # Fibonacci series: 斐波纳契数列
    # 两个元素的总和确定了下一个数
    a, b = 0, 1
    while b < 1000:
        # 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
        print(b, end=",")
        a, b = b, a + b
