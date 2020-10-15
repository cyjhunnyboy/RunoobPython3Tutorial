# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    行与缩进
        Python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}。
        缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
        缩进不一致，会导致运行错误
'''
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
