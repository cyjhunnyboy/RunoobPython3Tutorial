# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        数学函数
            函数	                返回值(描述)
            abs(x)	            返回数字的绝对值，如abs(-10)返回10
            ceil(x)	            返回数字的上入整数，如math.ceil(4.1)返回5
            cmp(x, y)           如果x<y返回-1，如果x==y返回0，如果x>y返回1，Python3已废弃。使用(x>y)-(x<y)替换。
            exp(x)	            返回e的x次幂(ex)，如math.exp(1)返回2.718281828459045
            fabs(x)	            返回数字的绝对值，如math.fabs(-10)返回10.0
            floor(x)	        返回数字的下舍整数，如math.floor(4.9)返回4
            log(x)	            如math.log(math.e)返回1.0，math.log(100,10)返回2.0
            log10(x)	        返回以10为基数的x的对数，如math.log10(100)返回2.0
            max(x1, x2,...)	    返回给定参数的最大值，参数可以为序列。
            min(x1, x2,...)	    返回给定参数的最小值，参数可以为序列。
            modf(x)	            返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
            pow(x, y)	        x**y 运算后的值。
            round(x [,n])	    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
            sqrt(x)	            返回数字x的平方根。

        Python3 abs() 函数
            描述：
                abs()函数返回数字的绝对值
            语法：
                abs(x)
                参数：
                    x -- 数值表达式，可以是整数，浮点数，复数。
            返回值：
                函数返回x(数字)的绝对值，如果参数是一个复数，则返回它的大小
"""
if __name__ == "__main__":
    print("abs(-40)：", abs(-40))
    print("abs(100.10)：", abs(100.10))
