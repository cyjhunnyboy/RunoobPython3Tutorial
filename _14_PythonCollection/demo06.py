# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合的基本操作 -- 移除元素
            此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误
                语法格式如下：
                    s.discard(x)：将元素x从集合s中移除，如果元素不存在，不会发生错误
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao"}

    # 通过discard(x)方法移除元素
    thisset.discard("Taobao")
    print(thisset)

    # 通过discard(x)方法移除元素
    # 不存在不会发生错误
    thisset.discard("Facebook")
    print(thisset)
