# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
try-finally 语句
    try-finally语句无论是否发生异常都将执行最后的代码。
    语法格式如下：
        try:
            执行代码
        except:
            发生异常时执行的代码
        else:
            没有异常时执行的代码
        finally:
            不管有没有发生异常都会执行的代码
'''
if __name__ == "__main__":
    try:
        runoob()
    except AssertionError as error:
        # 发生异常时执行的代码
        print(error)
    else:
        # 没有异常时执行的代码
        try:
            with open("file.log") as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        # 不管有没有发生异常都会执行的代码
        print("这句话，无论异常是否发生都会执行。")
