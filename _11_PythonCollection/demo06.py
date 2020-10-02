# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示
s.discard( x )
"""
thisset = {"Google", "Runoob", "Taobao"}
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)
