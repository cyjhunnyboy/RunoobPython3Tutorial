# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set discard()方法
                描述：
                    discard()方法用于移除指定的集合元素。
                    该方法不同于remove()方法，因为remove()方法在移除一个不存在的元素时会发生错误，而discard()方法不会。
                语法：
                    set.discard(value)
                    参数：
                        value -- 必需，要移除的元素
                返回值：
                    无
"""
if __name__ == "__main__":
    fruits = {"apple", "banana", "cherry"}

    print("执行discard(\"banana\")前集合fruits为：", fruits)
    # 移除集合中的元素banana
    fruits.discard("banana")
    print("执行discard(\"banana\")后集合fruits为：", fruits)

    # discard()方法删除不存在的元素不会报错
    fruits.discard("taozi")
    print("执行discard(\"taozi\")后集合fruits为：", fruits)
