# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 数组翻转指定个数的元素
    定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
    例如：(ar[], d, n)将长度为n的 数组arr的前面d个元素翻转到数组尾部。
'''


def leftRotate(arr, d, n):
    """将长度为n的 数组arr的前面d个元素翻转到数组尾部"""

    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    """将数组元素翻转到数组尾部"""

    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size):
    """打印数组元素"""

    for i in range(size):
        print("%d" % arr[i], end=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, 7)
    printArray(arr, 7)
