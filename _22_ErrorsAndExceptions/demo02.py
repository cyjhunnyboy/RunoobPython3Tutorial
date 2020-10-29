# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
异常处理
    try/except 语句
        异常捕捉可以使用try/except语句。
    格式：
        try:
            执行代码
        except:
            发生异常时执行的代码

        try语句按照如下方式工作；
            1、首先，执行try子句（在关键字try和关键字except之间的语句）
            2、如果没有异常发生，忽略except子句，try子句执行后结束。
            3、如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。
               如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。
            4、如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

    一个try语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
    处理程序将只针对对应的try子句中的异常进行处理，而不是其他的try的处理程序中的异常。

    一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如：
        except (RuntimeError, TypeError, NameError):
            pass
'''
if __name__ == "__main__":
    while True:
        try:
            x = int(input("请输入一个数字："))
            print("你输入的数字是：", x)
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
