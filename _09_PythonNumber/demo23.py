# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 uniform() 函数
            描述：
                uniform()方法将随机生成下一个实数，它在[x,y]范围内
            语法：
                import random
                random.uniform(x, y)
                参数：
                    x -- 随机数的最小值
                    y -- 随机数的最大值
            返回值：
                返回一个浮点数

        注意：uniform()是不能直接访问的，需要导入random模块，然后通过random静态对象调用该方法。
"""
import random

if __name__ == "__main__":
    print("uniform(5, 10)的随机浮点数：", random.uniform(5, 10))
    print("uniform(7, 14)的随机浮点数：", random.uniform(7, 14))
