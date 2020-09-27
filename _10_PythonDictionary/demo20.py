# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 字典 popitem() 方法
描述
Python 字典 popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。

如果字典已经为空，却调用了此方法，就报出KeyError异常。

语法
popitem()方法语法：

popitem()
参数
无
返回值
返回一个键值对(key,value)形式。
"""

site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.popitem()
print(pop_obj)
print(site)
