# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 条件控制
        Python 条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块
            if 嵌套
                在嵌套if语句中，可以把if...elif...else结构放在另外一个if...elif...else结构中
                    if 表达式1:
                        语句
                        if 表达式2：
                            语句
                        elif 表达式3:
                            语句
                        else:
                            语句
                    elif 表达式4:
                        语句
                    else:
                        语句
"""
if __name__ == "__main__":
    num = int(input("输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除2和3")
        else:
            print("你输入的数字可以整除2，但不能整除3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除3，但不能整除2")
        else:
            print("你输入的数字不能整除2和3")
