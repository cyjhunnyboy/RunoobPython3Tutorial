# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        随机数函数
            随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

        Python包含以下常用随机数函数
            choice(seq)：从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
            randrange([start,] stop [,step])：从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
            random()：随机生成下一个实数，它在[0,1)范围内。
            seed([x])：改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
            shuffle(lst)：将序列的所有元素随机排序
            uniform(x, y)：随机生成下一个实数，它在[x,y]范围内。

        Python3 choice() 函数
            描述：
                choice()方法返回一个列表，元组或字符串的随机项
            语法：
                import random
                random.choice(seq)
                参数：
                    seq -- 可以是一个列表，元组或字符串
            返回值：
                返回随机项

        注意：choice()是不能直接访问的，需要导入random模块，然后通过random静态对象调用该方法。
"""
import random

if __name__ == "__main__":
    print("从range(100)返回一个随机数：", random.choice(range(100)))
    print("从列表中[1, 2, 3, 5, 9])返回一个随机元素：", random.choice([1, 2, 3, 5, 9]))
    print("从字符串中'Runoob'返回一个随机字符：", random.choice('Runoob'))
