# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python赋值运算符（假设变量a为10，变量b为20）
    =：简单的赋值运算符，实例：c=a+b将a+b的运算结果赋值为c
    +=：加法赋值运算符，实例：c+=a等效于c=c+a
    -=：减法赋值运算符，实例：c-=a等效于c=c-a
    *=：乘法赋值运算符，实例：c*= a等效于c=c*a
    /=：除法赋值运算符，实例：c/=a等效于c=c/a
    %=：取模赋值运算符，实例：c%=a等效于c=c%a
    **=：幂赋值运算符，实例：c**=a等效于c=c**a
    //=：取整除赋值运算符，实例c//=a等效于c=c//a
'''
if __name__ == "__main__":
    a = 21
    b = 10
    c = 0

    c = a + b
    print("c = a + b 结果为：", c)

    c += a
    print("c += a 结果为：", c)

    c *= a
    print("c *= a 结果为：", c)

    c /= a
    print("c /= a 结果为：", c)

    c = 2
    c %= a
    print("c %= a 结果为：", c)

    c **= a
    print("c **= a 结果为：", c)

    c //= a
    print("c //= a 结果为：", c)
