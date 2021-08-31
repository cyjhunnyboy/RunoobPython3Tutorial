# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、多个语句构成代码组
            缩进相同的一组语句构成一个代码块，我们称之代码组。
            像if、while、def和class这样的复合语句，首行以关键字开始，以冒号(:)结束，该行之后的一行或多行代码构成代码组。
            我们将首行及后面的代码组称为一个子句(clause)。

            如下实例：
                if expression :
                   suite
                elif expression :
                   suite
                else :
                   suite
'''
if __name__ == "__main__":
    num = 12
    if num % 2 == 0:
        print("num = %d 是偶数" % num)
    else:
        print("num = %d是奇数" % num)
