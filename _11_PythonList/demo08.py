# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python列表函数&方法
            Python包含以下函数:
                len(list)列表元素个数
                max(list)返回列表元素最大值
                min(list)返回列表元素最小值
                list(seq)将元组转换为列表

            Python3 List len()方法
                描述：
                    len()方法返回列表元素个数。
                语法：
                    len(list)
                    参数：
                        list -- 要计算元素个数的列表
                返回值：返回列表元素个数
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao"]
    print("list1列表长度是：", len(list1))
    # 创建一个0-4的列表
    list2 = list(range(5))
    print("list2列表长度是：", len(list2))
