# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 seed() 函数
描述：seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数
语法：
import random
random.seed ([x])
注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
参数：x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed
返回值：本函数没有返回值
"""
import random

random.seed()
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
