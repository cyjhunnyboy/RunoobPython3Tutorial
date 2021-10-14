# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合的基本操作 -- 添加元素
            语法格式如下：
                s.add(x)：将元素x添加到集合s中，如果元素已存在，则不进行任何操作
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao"}

    # 通过add(x)方法添加元素
    thisset.add("Facebook")
    print(thisset)
