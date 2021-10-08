# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        del语句的语法是：
            del var1[,var2[,var3[...,varN]]]
"""
if __name__ == "__main__":
    # 您可以通过使用del语句删除单个或多个对象的引用
    var = 10
    var_a = 2.0
    var_b = 15.0
    print(var)
    print(var_a)
    print(var_b)
    del var
    del var_a, var_b
