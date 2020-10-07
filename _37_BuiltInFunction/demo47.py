# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
数字格式化
    str.format() 格式化数字的多种方法
'''
# 保留小数点后两位，格式：{:.2f}
print("{:.2f}".format(3.1415926))

# 带符号保留小数点后两位，格式：{:+.2f}
print("{:+.2f}".format(3.1415926))

# 带符号保留小数点后两位，格式：{:+.2f}
print("{:+.2f}".format(-1))

# 不带小数，格式：{:.0f}
print("{:.0f}".format(2.71828))
