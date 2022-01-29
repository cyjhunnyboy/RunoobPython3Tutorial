# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 摄氏温度转华氏温度
    摄氏温度转华氏温度的公式为：celsius * 1.8 = fahrenheit - 32，所以得到以下式子：
    celsius = (fahrenheit - 32) / 1.8
'''

if __name__ == "__main__":
    # 用户输入摄氏温度
    # 接收用户输入
    celsius = float(input("输入摄氏温度："))

    # 计算华氏温度
    fahrenheit = (celsius * 1.8) + 32
    print("%0.1f摄氏温度转为华氏温度为：%0.1f" % (celsius, fahrenheit))
