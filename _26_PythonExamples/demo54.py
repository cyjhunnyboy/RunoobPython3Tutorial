# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 实现秒表功能
'''
import time

if __name__ == "__main__":
    print("按下回车开始计时，按下Ctr+C停止计时。")
    while True:
        # 如果是Python 2.x版本请使用raw_input()
        input("")
        starttime = time.time()
        print("开始")
        try:
            while True:
                print("计时：", round(time.time() - starttime, 0), "秒", end="\r")
                time.sleep(1)
        except KeyboardInterrupt:
            print("结束")
            endtime = time.time()
            print("总共的时间为：", round(endtime - starttime, 2), "secs")
            break
