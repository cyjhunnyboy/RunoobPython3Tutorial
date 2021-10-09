# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List insert()方法
            描述：
                insert()函数用于将指定对象插入列表的指定位置
            语法：
                list.insert(index, obj)
                参数：
                    index -- 对象obj需要插入的索引位置
                    obj -- 要插入列表中的对象
            返回值：
                该方法没有返回值，但会在列表指定位置插入对象
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao"]
    list1.insert(1, "Baidu")
    print("列表插入元素后为：", list1)
