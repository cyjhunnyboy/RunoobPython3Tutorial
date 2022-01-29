# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
使用 flush 参数生成一个 Loading 的效果
'''
import time

if __name__ == "__main__":
    print("---RUNOOB EXAMPLE ： Loading 效果---")
    print("Loading", end="")
    for i in range(20):
        print(".", end='', flush=True)
        time.sleep(0.5)
