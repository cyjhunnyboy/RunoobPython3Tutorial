# -*- coding: UTF-8 -*-
# author: chenyongjun
import sys

"""
错误输出重定向和程序终止
sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息
"""
sys.stderr.write('Warning, log file not found starting a new one\n')
