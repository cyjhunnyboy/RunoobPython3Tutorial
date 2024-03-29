# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、Number（数字）
            Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示，
            复数的实部a和虚部b都是浮点型
            数值类型实例
            int              float                 complex
            10               0.0                    3.14j
            100              15.20                  45.j
            -786             -21.9                  9.322e-36j
            080              32.3e+18               .876j
            -0490            -90.                   -.6545+0J
            -0x260           -32.54e100             3e+26J
            0x69             70.2E-12               4.53e-7j
"""
if __name__ == "__main__":
    a = -0x260
    b = 32.3e+18
    c = 4.53e-7j

    print(a)
    print(b)
    print(c)
