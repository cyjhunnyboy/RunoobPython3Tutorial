# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set update()方法
                描述：
                    update()方法用于修改当前集合，可以添加新的元素或集合到当前集合中，
                    如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
                语法：
                    set.update(set)
                    参数：
                        set -- 必需，可以是元素或集合。
                返回值：
                    无。
"""
if __name__ == "__main__":
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}

    # 添加新的元素或集合到当前集合中，已处在会忽略
    x.update(y)

    print(x)
    print(y)
