# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python支持三种不同的数值类型：
            整型(Int)：通常被称为是整型或整数，是正或负整数，不带小数点。
                      Python3整型是没有限制大小的，可以当作Long类型使用，
                      所以Python3没有Python2的Long类型。布尔(bool)是整型的子类型。
            浮点型(float)：浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2=2.5x102=250）
            复数(complex)：复数由实数部分和虚数部分构成，可以用a+bj，或者complex(a,b)表示，复数的实部a和虚部b都是浮点型。
"""
if __name__ == "__main__":
    # 十六进制
    number = 0xA0F
    print(number)
    # 八进制
    number = 0o37
    print(number)

    # int
    print(10)
    # float
    print(0.0)
    # complex
    print(3.14j)

    # int
    print(100)
    # float
    print(15.20)
    # complex
    print(45.j)

    # int
    print(-786)
    # float
    print(-21.9)
    # complex
    print(9.322e-36j)

    # int
    print(0o10)
    # float
    print(32.3e+18)
    # complex
    print(.876j)

    # int
    print(-0o47)
    # float
    print(-90.)
    # complex
    print(-.6545 + 0J)

    # int
    print(-0x260)
    # float
    print(-32.54e100)
    # complex
    print(3e+26J)

    # int
    print(0x69)
    # float
    print(70.2E-12)
    # complex
    print(4.53e-7j)
