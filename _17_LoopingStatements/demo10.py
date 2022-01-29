# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while

        break和continue语句及循环中的else子句
            代码执行过程如下：
            while <expre>:
                <statement>
                <statement>
                break
                <statement>
                <statement>
                continue
                <statement>
                <statement>
            <statement>
            break语句可以跳出for和while的循环体。如果你从for或while循环中终止，任何对应的循环else块将不执行
            continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
"""
if __name__ == "__main__":
    # while中使用continue
    n = 5
    while n > 0:
        n -= 1
        if n == 2:
            continue
        print(n)
    print("循环结束。")
