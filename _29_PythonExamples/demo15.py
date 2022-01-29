# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python if 语句
    使用if...elif...else语句判断数字是正数、负数或零
    优化增加输入字符的判断以及异常输出
'''


def assure():
    """判断数字是正数、负数或零"""

    while True:
        try:
            # 用户输入数字
            num = float(input("请输入一个数字："))

            # 判断该数字是正数、负数或零
            if num > 0:
                print("正数")
            elif num == 0:
                print("正数")
            else:
                print("负数")
            break
        except ValueError:
            print("输入无效，需要输入一个数字。")


if __name__ == "__main__":
    # 判断该数字是正数、负数或零
    assure()
