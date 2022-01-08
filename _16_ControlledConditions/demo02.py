# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 条件控制
        Python 条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块
            if 语句
                Python中if语句的一般形式如下所示：

                    if condition_1:
                        statement_block_1
                    elif condition_2:
                        statement_block_2
                    else:
                        statement_block_3

                    如果"condition_1"为True将执行"statement_block_1"块语句
                    如果"condition_1"为False将判断"condition_2"
                    如果"condition_2"为True将执行"statement_block_2"块语句
                    如果"condition_2"为False将执行"statement_block_3"块语句

                Python中用elif代替了else if，所以if语句的关键字为：if–elif–else

                注意：
                    1、每个条件后面要使用冒号:，表示接下来是满足条件后要执行的语句块。
                    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
                    3、在Python中没有switch–case语句。
"""
if __name__ == "__main__":
    # if 语句
    var1 = 100
    if var1:
        print("1-if表达式条件为true")
        print(var1)

    # if 语句
    var2 = 0
    # var2为0，即为false，if内的语句没有执行
    if var2:
        print("2-if表达式条件为true")
        print(var2)
    print("Good bye!")
