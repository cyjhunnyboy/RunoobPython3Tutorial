# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
__init__() 构造方法
    __init__()是类的特殊方法（构造方法），该方法在类实例化时会自动调用
     __init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上
'''


class Complex:

    def __init__(self, realpart, imagpart):
        self.realpart = realpart
        self.imagpart = imagpart

    def print_complex(self):
        print("realpart = {0:.1f}, imagpart = {1:.2f}".format(self.realpart, self.imagpart))


if __name__ == "__main__":
    x = Complex(3.0, -4.5)
    # 输出结果：realpart = 3.0, imagpart = -4.50
    x.print_complex()
