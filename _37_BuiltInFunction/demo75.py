# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python memoryview() 函数
描述：
    memoryview() 函数返回给定参数的内存查看对象(memory view)
    所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问
语法：
    memoryview(obj)
    参数说明：
        obj -- 对象
返回值：
    返回元组列表
'''
if __name__ == "__main__":
    # Python 2.x应用
    # v = memoryview('abcefg')
    v = memoryview(bytearray("abcefg", 'utf-8'))
    print(v[1])
    print(v[-1])
    print(v[1:4])
    print(v[1:4].tobytes())
