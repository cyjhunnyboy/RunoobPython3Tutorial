# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List index()方法
            描述：index()函数用于从列表中找出某个值第一个匹配项的索引位置
            语法：
                list.index(x[, start[, end]])
                参数
                    x-- 查找的对象
                    start-- 可选，查找的起始位置
                    end-- 可选，查找的结束位置
            返回值
                该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao"]
    print('Runoob索引值为：', list1.index("Runoob"))
    print('Taobao索引值为：', list1.index("Taobao"))

    list2 = ["Google", "Runoob", "Taobao", "Facebook", "QQ"]
    # 从指定位置开始搜索
    print("Runoob索引值为：", list2.index("Runoob", 1))
