# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基础语法
        1、多行语句
            Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
            在[], {}, 或()中的多行语句，不需要使用反斜杠(\)
"""
if __name__ == "__main__":
    # Python通常是一行写完一条语句
    item_one = "Hello"
    item_two = " Welcome"
    item_third = " to Python!"

    # 但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
    total = item_one + \
            item_two + \
            item_third

    print(total)

    # 在[], {}, 或()中的多行语句，不需要使用反斜杠(\)
    total_all = ["item_one", "item_two", "item_three",
                 "item_four", "item_five"]

    print(total_all)
