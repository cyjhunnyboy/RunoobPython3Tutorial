# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python eval() 函数
描述：
    eval() 函数用来执行一个字符串表达式，并返回表达式的值
语法：
    eval(expression[, globals[, locals]])
    参数：
        1、expression -- 表达式。
        2、globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
        3、locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
返回值：
    返回表达式计算结果
'''
if __name__ == "__main__":
    x = 7
    print(eval("3 * x"))
    print(eval("pow(2, 2)"))
    n = 81
    print(eval("n + 4"))
