# -*- coding: UTF-8 -*-
# author: chenyongjun
import random

"""
数学
math模块为浮点运算提供了对底层C函数库的访问
"""

print(random.choice(["apple", "pear", "banana"]))
print(random.sample(range(100), 10))  # sampling without replacement
print(random.random())  # random float
print(random.randrange(6))  # random integer chosen from range(6)
