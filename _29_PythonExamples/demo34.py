# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 生成日历
'''
# 引入日历模块
import calendar

if __name__ == "__main__":
    # 输入指定年月
    yy = int(input("输入年份："))
    mm = int(input("输入月份："))

    # 显示日历
    print(calendar.month(yy, mm))
