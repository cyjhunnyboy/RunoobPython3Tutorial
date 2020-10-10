# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python slice() 函数
描述：
    slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
语法：
    class slice(stop)
    class slice(start, stop[, step])
    参数说明：
        start -- 起始位置
        stop -- 结束位置
        step -- 间距
返回值：
    返回一个切片对象
'''
if __name__ == "__main__":
    # 设置截取5个元素的切片
    myslice = slice(5)
    print(myslice)

    arr = range(10)
    for i in arr:
        print(i)

    print("==============")
    arr2 = arr[myslice]
    for j in arr2:
        print(j)
