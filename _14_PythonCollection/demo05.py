# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合的基本操作 -- 移除元素
            语法格式如下：
                s.remove(x)：将元素x从集合s中移除，如果元素不存在，则会发生错误
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao"}

    # 通过remove(x)方法移除元素
    thisset.remove("Taobao")
    print(thisset)

    # 不存在会发生错误
    # KeyError: 'Facebook'
    thisset.remove("Facebook")
