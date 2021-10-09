# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 splitlines()方法
            描述：
                splitlines()按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数keepends为False，
                不包含换行符，如果为True，则保留换行符
            语法：
                str.splitlines([keepends])
                参数：
                    keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为False，不包含换行符，如果为True，则保留换行符
            返回值：
                返回一个包含各行作为元素的列表
"""
if __name__ == "__main__":
    print('ab c\n\nde fg\rkl\r\n'.splitlines())
    print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
