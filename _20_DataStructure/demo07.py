# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数据结构
        元组和序列
            元组由若干逗号分隔的值组成

            元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号，
            不过括号通常是必须的（如果元组是更大的表达式的一部分）
"""
if __name__ == "__main__":
    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)

    # Tuples may be nested
    u = t, (1, 2, 3, 4, 5)
    print(u)
