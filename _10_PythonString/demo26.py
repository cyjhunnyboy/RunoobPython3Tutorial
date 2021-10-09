# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 join()方法
            描述：
                join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
            语法：
                str.join(sequence)
                参数：
                    sequence -- 要连接的元素序列
            返回值：
                返回通过指定字符连接序列中元素后生成的新字符串
"""
if __name__ == "__main__":
    s1 = "-"
    s2 = ""
    seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
    print(s1.join(seq))
    print(s2.join(seq))
