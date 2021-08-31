# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、数字(Number)类型
            Python中数字有四种类型：整数、布尔型、浮点数和复数。
            int(整数), 如1, 只有一种整数类型int，表示为长整型，没有Python2中的Long。
            bool(布尔), 如 True。
            float(浮点数), 如 1.23、3E-2
            complex(复数), 如 1 + 2j、 1.1 + 2.2j
'''
if __name__ == "__main__":
    # 整数
    int_1 = 100
    print(int_1)

    # 布尔
    bool_1 = True
    bool_2 = False
    print(bool_1)
    print(bool_2)

    # 浮点数
    float_1 = 1.23
    float_2 = 3E-2
    print(float_1)
    print(float_2)

    # 复数
    complex_1 = 1 + 2j
    complex_2 = 1.1 + 2.2j
    print(complex_1)
    print(complex_2)
