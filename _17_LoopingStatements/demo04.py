# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while
        while循环使用else语句
            在while … else在条件语句为false时执行else的语句块
            语法格式如下：
                while <expr>:
                    <statement(s)>
                else:
                    <additional_statement(s)>
                expr条件语句为true则执行statement(s)语句块，如果为false，则执行additional_statement(s)。
"""
if __name__ == "__main__":
    # 循环输出数字，并判断大小
    count = 0
    while count < 5:
        print(count, "小于5")
        count = count + 1
    else:
        print(count, "大于或等于5")
