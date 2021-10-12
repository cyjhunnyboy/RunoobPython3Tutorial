# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        删除字典元素
            能删单一的元素也能清空字典，清空只需一项操作。
            显示删除一个字典用del命令
"""
if __name__ == "__main__":
    dict_1 = {"Name": "Runoob", "Age": 7, "Class": "First"}

    # 删除键"Name"
    del dict_1["Name"]

    # 清空字典
    dict_1.clear()

    # 删除字典
    del dict_1

    # NameError: name 'dict_1' is not defined
    print("dict_1['Age']: ", dict_1["Age"])
    # KeyError: 'Class'
    print("dict_1['Class']: ", dict_1["Class"])
