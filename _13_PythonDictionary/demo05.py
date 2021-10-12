# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典键的特性
            字典值可以是任何的Python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
            两个重要的点需要记住：
                1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
                2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""
if __name__ == "__main__":
    # 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    dict_1 = {"Name": "Runoob", "Age": 7, "Name": "小菜鸟"}
    # 输出结果为：dict_boy['Name']:  小菜鸟
    print("dict_1['Name']: ", dict_1["Name"])

    # 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
    # TypeError: unhashable type: 'list'
    dict_2 = {["Name"]: "Runoob", "Age": 7}
    print("dict_2['Name']: ", dict_2["Name"])
