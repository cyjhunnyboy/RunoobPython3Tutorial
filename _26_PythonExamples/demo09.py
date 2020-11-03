# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 随机数生成
    生成0~9之间的随机数，需要导入random(随机数)模块
    使用了random模块的randint()函数来生成随机数，你每次执行后都返回不同的数字（0 到 9）
    该函数的语法为：
        random.randint(a,b)
        函数返回数字N，N为a到b之间的数字（a <= N <= b），包含a和b
'''
import random

if __name__ == "__main__":
    # 调用方法
    randomNum = random.randint(0, 9)
    print("生成0~9之间的随机数为：", randomNum)
