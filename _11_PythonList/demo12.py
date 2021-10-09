# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List append()方法
            描述：
                append()方法用于在列表末尾添加新的对象
            语法：
                list.append(obj)
                参数：
                    obj -- 添加到列表末尾的对象
            返回值
                该方法无返回值，但是会修改原来的列表
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao"]
    list1.append('Baidu')
    print("更新后的列表：", list1)
