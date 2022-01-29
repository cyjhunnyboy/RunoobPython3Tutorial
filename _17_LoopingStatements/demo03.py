# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while
        while循环
            Python中while语句的一般形式：
            while 判断条件(condition)：
                执行语句(statements)……

        同样需要注意冒号和缩进。另外，在Python中没有do..while循环

        无限循环
            设置条件表达式永远不为false来实现无限循环
            使用CTRL+C来退出当前的无限循环
            无限循环在服务器上客户端的实时请求非常有用
"""
if __name__ == "__main__":
    var = 1
    # 表达式永远为 true
    while var == 1:
        num = int(input("输入一个数字："))
        print("你输入的数字是：", num)

    print("Good bye!")
