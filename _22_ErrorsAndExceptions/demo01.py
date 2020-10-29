# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
    Python有两种错误很容易辨认：语法错误和异常。
    Python assert（断言）用于判断一个表达式，在表达式条件为false的时候触发异常。

    语法错误
        Python的语法错误或者称之为解析错，是初学者经常碰到的。例如：
        while True print('Hello world')

        File "<stdin>", line 1, in ?
        while True print('Hello world')
                        ^
        SyntaxError: invalid syntax
        函数print()被检查到有错误，是它前面缺少了一个冒号:
        语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

    异常
        即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
        大多数的异常都不会被程序处理，都以错误信息的形式展现在这里

        异常以不同的类型出现，这些类型都作为信息的一部分打印出来
        例子中的类型有ZeroDivisionError，NameError和TypeError。
        错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。
'''
if __name__ == "__main__":
    # 0不能作为除数
    # 触发异常ZeroDivisionError
    print(10 * (1 / 0))
    # spam未定义，触发异常NameError
    print(4 + spam * 3)
    # int不能与str相加，触发异常TypeError
    a = '2' + 2
    print(a)
