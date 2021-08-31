# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python数据类型转换
        Python complex()函数
            描述：
                complex()用于创建一个值为real+imag*j 的复数或者转化一个字符串或数为复数。
                如果第一个参数为字符串，则不需要指定第二个参数

            语法：
                class complex([real[,imag]])
                参数：
                    real -- int, long, float或字符串；
                    imag -- int, long, float；
            返回值：
                返回一个复数。
'''
if __name__ == "__main__":
    print(complex(1, 2))
    # 数字
    print(complex(1))
    # 当做字符串处理
    print(complex("1"))
    # 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
    print(complex("1+2j"))
