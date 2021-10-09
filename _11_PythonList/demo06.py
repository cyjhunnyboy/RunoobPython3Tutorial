# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python列表截取与拼接
            Python的列表截取与字符串操作类型
"""
if __name__ == "__main__":
    L = ["Google", "Runoob", "Taobao"]
    # 读取第三个元素
    print(L[2])
    # 从右侧开始读取倒数第二个元素
    print(L[-2])
    # 输出从第二个元素开始后的所有元素
    print(L[1:])

    # 列表还支持拼接操作
    squares = [1, 4, 9, 16, 25]
    squares += [36, 49, 64, 81, 100]
    print(squares)
