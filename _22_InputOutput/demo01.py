# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
输出格式美化
    Python两种输出值的方式: 表达式语句和print()函数。
    第三种方式是使用文件对象的write()方法，标准输出文件可以用sys.stdout引用。
    如果你希望输出的形式更加多样，可以使用str.format()函数来格式化输出值。
    如果你希望将输出的值转成字符串，可以使用repr()或 str()函数来实现。

    str()：函数返回一个用户易读的表达形式。
    repr()：产生一个解释器易读的表达形式
'''
if __name__ == "__main__":
    s = "Hello, Runoob"
    print(str(s))
    print(repr(s))
    print(str(1 / 7))

    x = 10 * 3.25
    y = 200 * 200
    s = "x 的值为： " + repr(x) + "，y 的值为：" + repr(y) + "..."
    print(s)

    # repr()函数可以转义字符串中的特殊字符
    hello = "hello, runoob\n"
    print(repr(hello))

    # repr()的参数可以是Python的任何对象
    print(repr((x, y, ("Google", "Runoob"))))

    # 一个平方与立方
    for x in range(1, 11):
        # 字符串对象的rjust()方法，它可以将字符串靠右，并在左边填充空格
        # 还有类似的方法，如ljust()和center()。这些方法并不会写任何东西，它们仅仅返回新的字符串
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
        # 注意前一行"end"的使用
        print(repr(x * x * x).rjust(4))

    # 一个平方与立方
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

    # 方法zfill()它会在数字的左边填充0
    print('12'.zfill(5))
    print('-3.14'.zfill(7))
    print('3.14159265359'.zfill(5))
