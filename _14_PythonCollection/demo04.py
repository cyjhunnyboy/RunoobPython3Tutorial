# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合的基本操作 -- 添加元素
            还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，
                语法格式如下：
                    s.update(x)：x可以有多个，用逗号分开，如果元素已存在，则不进行任何操作
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao"}

    # 通过update(x)方法更新元素
    thisset.update({1, 3})
    print(thisset)

    # 通过update(x)方法更新元素
    thisset.update([1, 4], [5, 6])
    print(thisset)
