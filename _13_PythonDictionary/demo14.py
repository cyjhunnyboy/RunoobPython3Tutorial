# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        直接赋值、浅拷贝和深度拷贝解析
            1、直接赋值：其实就是对象的引用（别名）。
            2、浅拷贝（copy）：拷贝父对象，不会拷贝对象的内部的子对象。
            3、深拷贝（deepcopy）：copy模块的deepcopy方法，完全拷贝了父对象及其子对象。
"""
import copy

if __name__ == "__main__":
    # 原始对象
    a = [1, 2, 3, 4, ["a", "b"]]

    b = a                   # 赋值，传对象的引用
    c = copy.copy(a)        # 对象拷贝，浅拷贝
    d = copy.deepcopy(a)    # 对象拷贝，深拷贝

    a.append(5)             # 修改对象
    a[4].append("c")        # 修改对象a中的["a", "b"]数组对象

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print("a的id是：", id(a))
    print("a的a[4]元素的id是：", id(a[4]))
    print("b的id是：", id(b))
    print("b的b[4]元素的id是：", id(b[4]))
    print("c的id是：", id(d))
    print("c的c[4]元素的id是：", id(c[4]))
    print("d的id是：", id(d))
    print("d的d[4]元素的id是：", id(d[4]))
