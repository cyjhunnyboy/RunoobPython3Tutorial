# -*- coding: UTF-8 -*-
# author: chenyongjun
import re

"""
字符串正则匹配
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案
"""
find_all = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(find_all)
result_sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(result_sub)
