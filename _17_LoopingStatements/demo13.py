# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        循环语句可以有else子句，它在穷尽列表(以for循环)或条件变为false(以while循环)
       导致循环终止时被执行，但循环被break终止时不执行
"""
if __name__ == "__main__":
    # 查询质数的循环例子
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, "等于", x, "*", n // x)
                break
        else:
            # 循环中没有找到元素
            print(n, ' 是质数')
