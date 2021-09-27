# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python赋值运算符
            假设变量a为10，变量b为20
            =      简单的赋值运算符（c=a+b将a+b的运算结果赋值为c）
            +=     加法赋值运算符（c+=a等效于c=c+a）
            -=     减法赋值运算符（c-=a等效于c=c-a）
            *=     乘法赋值运算符（c*= a等效于c=c*a）
            /=     除法赋值运算符（c/=a等效于c=c/a）
            %=     取模赋值运算符（c%=a等效于c=c%a）
            **=    幂赋值运算符（c**=a等效于c=c**a）
            //=    取整除赋值运算符（c//=a等效于c=c//a）
            :=     海象运算符，可在表达式内部为变量赋值，Python3.8版本新增运算符
                  （在这个运算符中，赋值表达式可以避免调用len()两次：
                  if(n:=len(a))>10: print(f"List is too long ({n} elements, expected <= 10)")
"""
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
