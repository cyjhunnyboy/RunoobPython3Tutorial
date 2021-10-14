# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        判断元素是否在集合中存在
            语法格式如下：
                x in s：判断元素x是否在集合s中，存在返回True，不存在返回False
"""
if __name__ == "__main__":
    thisset = {"Google", "Runoob", "Taobao"}

    print(thisset)
    # 判断元素是否在集合中
    print("Runoob 是否在集合中：", "Runoob" in thisset)
    print("Facebook 是否在集合中：", "Facebook" in thisset)
