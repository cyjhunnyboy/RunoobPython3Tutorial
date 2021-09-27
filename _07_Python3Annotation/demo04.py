# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 注释
        确保对模块, 函数, 方法和行内注释使用正确的风格
        Python中的注释有单行注释和多行注释。
        文档注释，在方法体内进行多行注释
"""


def test():
    """这是文档字符串"""
    pass


if __name__ == "__main__":
    # 打印文档注释
    print(test.__doc__)
