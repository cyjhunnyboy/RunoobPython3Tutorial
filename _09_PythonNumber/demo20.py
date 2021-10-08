# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 randrange() 函数
        描述：
            randrange()方法返回指定递增基数集合中的一个随机数，基数缺省值为1
        语法：
            import random
            random.randrange ([start,] stop [,step])
            参数：
                start -- 指定范围内的开始值，包含在范围内。
                stop -- 指定范围内的结束值，不包含在范围内。
                step -- 指定递增基数。
        返回值：
            从给定的范围返回随机项

        注意：randrange()是不能直接访问的，需要导入random模块，然后通过random静态对象调用该方法。
"""
import random

if __name__ == "__main__":
    # 从 1-100 中选取一个奇数
    print("randrange(1,100, 2)：", random.randrange(1, 100, 2))

    # 从 0-99 选取一个随机数
    print("randrange(100)：", random.randrange(100))
