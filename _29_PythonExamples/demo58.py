# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 数组翻转指定个数的元素
    定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
    例如：(ar[], d, n)将长度为n的 数组arr的前面d个元素翻转到数组尾部。
'''


def leftRotate(arr, d, n):
    """将长度为n的 数组arr的前面d个元素翻转到数组尾部"""

    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd(a, b):
    """将数组元素翻转到数组尾部"""

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def printArray(arr, size):
    """打印数组元素"""

    for i in range(size):
        print("%d" % arr[i], end=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, 7)
    printArray(arr, 7)
