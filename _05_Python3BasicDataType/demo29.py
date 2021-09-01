# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        Python tuple()函数
            描述：
                tuple函数将列表转换为元组
            语法：
                tuple(seq)
                参数：
                    seq -- 要转换为元组的序列
            返回值：
                返回元组
"""
if __name__ == "__main__":
    list1 = ["Google", "Taobao", "Runoob", "Baidu"]
    tuple1 = tuple(list1)
    print(tuple1)
