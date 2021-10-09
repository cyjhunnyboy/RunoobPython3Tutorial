# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 strip()方法
            描述：
                strip()方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
                注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
            语法：
                str.strip([chars])
                参数：
                    chars -- 移除字符串头尾指定的字符序列
            返回值：
                返回移除字符串头尾指定的字符序列生成的新字符串
"""
if __name__ == "__main__":
    str_a = "*****this is **string** example....wow!!!*****"
    # 指定字符串 *
    print(str_a.strip('*'))

    str_b = "123abcrunoob321"
    # 字符序列为 12
    print(str_b.strip('123'))
