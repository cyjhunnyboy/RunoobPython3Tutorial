# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合的基本操作 -- 移除元素
            语法格式如下：
                s.pop()：随机删除集合中的一个元素
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao", "Facebook"}

    # 多次执行测试结果都不一样
    # set集合的pop方法会对集合进行无序的排列
    # 然后将这个无序排列集合的左面第一个元素进行删除
    thisset.pop()
    print(thisset)
