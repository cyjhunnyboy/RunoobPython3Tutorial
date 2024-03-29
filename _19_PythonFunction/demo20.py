# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        变量作用域
            Python中，程序的变量并不是在哪个位置都可以访问的，
            访问权限决定于这个变量是在哪里赋值的。
            变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
            L （Local） 局部作用域
            E （Enclosing） 闭包函数外的函数中
            G （Global） 全局作用域
            B （Built-in） 内建作用域
            以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找
"""
# 内建作用域
x = int(2.9)

# 全局作用域
g_count = 0


def outer():
    # 闭包函数外的函数中
    o_count = 1
    print("o_count = ", o_count)

    def inner():
        # 局部作用域
        i_count = 2
        print("i_count = ", i_count)


if __name__ == "__main__":
    print("x = ", x)
    print("g_count = ", g_count)
    outer()
