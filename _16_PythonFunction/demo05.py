# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 函数
参数传递
    在python中，类型属于对象，变量是没有类型的
    a=[1,2,3]
    a="Runoob"
    以上代码中，[1,2,3]是List类型，"Runoob"是String类型，而变量a是没有类型，她仅仅是一个对象的引用（一个指针），
    可以是指向List类型对象，也可以是指向String类型对象。

可更改(mutable)与不可更改(immutable)对象
    在python中，strings, numbers和tuples是不可更改的对象，而list, dict等则是可以修改的对象。
    不可变类型：变量赋值a=5后再赋值a=10，这里实际是新生成一个int值对象10，再让a指向它，
              而5被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值la=[1,2,3,4] 后再赋值la[2]=5则是将list la的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

    python函数的参数传递：
        不可变类型：类似c++的值传递，如整数、字符串、元组。如fun(a)，传递的只是a的值，没有影响a对象本身。
                  如果在fun(a)内部修改a的值，只是修改另一个复制的对象，不会影响a本身。
        可变类型：类似c++的引用传递，如 列表，字典。如 fun(la)，则是将la真正的传过去，修改后fun外部的la也会受影响

    python中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''


# 可写函数说明
def changeme(mylist):
    """传可变对象实例"""

    # 修改传入的列表
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


if __name__ == "__main__":
    # 调用changeme函数
    myList = [10, 20, 30]
    print("调用changeme函数前列表为：", myList)
    # 可变对象在函数里修改了参数，
    # 那么在调用这个函数的函数里，原始的参数也被改变了
    changeme(myList)
    # 传入函数的和在末尾添加新内容的对象用的是同一个引用
    print("函数外取值：", myList)
