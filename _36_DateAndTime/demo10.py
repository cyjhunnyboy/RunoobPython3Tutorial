# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
time.gmtime([secs])
接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
"""
import time

t = time.gmtime(1455508609.34375)
print("gmtime :", t)
print("时间戳（1455508609.34375）格式化后显示为：", time.strftime("%Y-%m-%d %H:%M:%S", t))
