# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
if 嵌套
    在嵌套if语句中，可以把if...elif...else结构放在另外一个if...elif...else结构中
'''
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
