# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python比较运算符
            假设变量a为10，变量b为20
            所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意这些变量名的大写。
            ==    等于：比较对象是否相等【(a==b)返回False】
            !=    不等于：比较两个对象是否不相等【(a!= b)返回True】
            >     大于：返回x是否大于y【(a>b)返回False】
            <     小于：返回x是否小于y【(a<b)返回True】
            >=    大于等于：返回x是否大于等于y【(a>=b)返回False】
            <=    小于等于：返回x是否小于等于y【(a<=b)返回True】
"""
if __name__ == "__main__":
    a = 21
    b = 10
    c = 0

    if a == b:
        print("a == b 结果为：")
    else:
        print("a == b 结果为：")

    if a != b:
        print("a != b 结果为：")
    else:
        print("a != b 结果为：")

    if a < b:
        print("a < b 结果为：")
    else:
        print("a < b 结果为：")

    if a > b:
        print("a > b 结果为：")
    else:
        print("a > b 结果为：")

    # 修改变量 a 和 b 的值
    a = 5
    b = 20
    if a <= b:
        print("a <= b 结果为：")
    else:
        print("a <= b 结果为：")

    if b >= a:
        print("b >= a 结果为：")
    else:
        print("b >= a 结果为：")
