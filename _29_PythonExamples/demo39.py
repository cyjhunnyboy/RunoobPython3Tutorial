# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算每个月天数
    导入calendar模块来计算每个月的天数
'''
import calendar

if __name__ == "__main__":
    monthRange = calendar.monthrange(2016, 9)
    print(monthRange)
