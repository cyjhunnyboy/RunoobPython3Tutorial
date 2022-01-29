# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while

        for语句
            Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
            for循环的一般格式如下：
                for <variable> in <sequence>:
                    <statements>
                else:
                    <statements>
"""
if __name__ == "__main__":
    # for实例中使用了break语句，break语句用于跳出当前循环体
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程！")
            break
        print("循环数据：" + site)
    else:
        print("没有循环数据！")
    print("完成循环！")
