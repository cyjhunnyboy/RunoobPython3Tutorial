# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 获取最大值函数
    使用max()方法求最大值
'''
if __name__ == "__main__":
    # 最简单的
    print("1, 2最大值为：", max(1, 2))
    print("a, b最大值为：", max('a', 'b'))

    # 也可以对列表和元组使用
    print("[1, 2]最大值为：", max([1, 2]))
    print("(1, 2)最大值为：", max((1, 2)))

    # 更多实例
    print("80, 100, 1000最大值为：", max(80, 100, 1000))
    print("-20, 100, 400最大值为：", max(-20, 100, 400))
    print("-80, -20, -10最大值为：", max(-80, -20, -10))
    print("0, 100, -400最大值为：", max(0, 100, -400))