# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        更新列表
            你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
"""
if __name__ == "__main__":
    list_a = ["Google", "Runoob", 1997, 2000]
    print("第三个元素为：", list_a[2])
    list_a[2] = 2001
    print("更新后的第三个元素为：", list_a[2])
