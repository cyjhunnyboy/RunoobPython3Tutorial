# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断闰年
    判断用户输入的年份是否为闰年，整百年能被400整除的是闰年，非整百年能被4整除的为闰年
'''


def is_leapyear(year):
    """判断用户输入的年份是否为闰年"""

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                # 整百年能被400整除的是闰年
                print("{0}是闰年".format(year))
            else:
                print("{0}不是闰年".format(year))
        else:
            # 非整百年能被4整除的为闰年
            print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))


if __name__ == "__main__":
    year = int(input("请输入一个年份："))

    # 判断用户输入的年份是否为闰年
    is_leapyear(year)
