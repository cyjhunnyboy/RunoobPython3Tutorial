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
import math

if __name__ == "__main__":
    # str.format() 的基本使用
    # 括号及其里面的字符(称作格式化字段)将会被format()中的参数替换
    print('{}网址："{}!"'.format("菜鸟教程", "www.runoob.com"))

    # 在括号中的数字用于指向传入对象在format()中的位置
    print("{0}和{1}".format("Google", "Runoob"))
    print("{1}和{0}".format("Google", "Runoob"))

    # 如果在format()中使用了关键字参数, 那么它们的值会指向使用该名字的参数
    print("{name}网址：{site}".format(name="菜鸟教程", site="www.runoob.com"))

    # 位置及关键字参数可以任意的结合
    print("站点列表：{0}, {1}, 和 {other}。".format("Google", "Runoob", other="Taobao"))

    # "!a"(使用ascii()), "!s" (使用str())和"!r"(使用repr())可以用于在格式化某个值之前对其进行转化
    print("常量PI的值近似为：{}。".format(math.pi))
    print("常量PI的值近似为：{!r}。".format(math.pi))

    # 可选项":"和格式标识符可以跟着字段名。这就允许对值进行更好的格式化
    print("常量PI的值近似为：{0:.3f}。".format(math.pi))

    # 在":"后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
    table = {"Google": 1, "Runoob": 2, "Taobao": 3}
    for name, number in table.items():
        print("{0:10} ==> {1:10}".format(name, number))

    # 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
    # 最简单的就是传入一个字典, 然后使用方括号"[]"来访问键值
    print("Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}".format(table))
    # 通过在table变量前使用**来实现相同的功能
    print("Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}".format(**table))
