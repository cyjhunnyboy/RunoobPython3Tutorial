# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 数组翻转指定个数的元素
    定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
    例如：(ar[], d, n)将长度为n的 数组arr的前面d个元素翻转到数组尾部。
'''


def rverseArray(arr, start, end):
    """将数组元素翻转到数组尾部"""

    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


def leftRotate(arr, d):
    """将长度为n的 数组arr的前面d个元素翻转到数组尾部"""

    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)


def printArray(arr):
    """打印数组元素"""

    for i in range(0, len(arr)):
        print(arr[i], end=' ')


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2)
    printArray(arr)
