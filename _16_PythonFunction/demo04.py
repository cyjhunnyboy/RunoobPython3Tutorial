# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
参数传递
在 python 中，类型属于对象，变量是没有类型的
a=[1,2,3]
a="Runoob"

以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
可以是指向 List 类型对象，也可以是指向 String 类型对象。

可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
          比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""
# python 传不可变对象实例


def change_int(a):
    a = 10
    print(a)


b = 2
change_int(b)
print(b)  # 结果是 2


# 可写函数说明
def change_me(my_list):
    """修改传入的列表"""
    my_list.append([1, 2, 3, 4])
    print("函数内取值: ", my_list)
    return


# 调用change_me函数
parm_list = [10, 20, 30]
change_me(parm_list)
print("函数外取值: ", parm_list)


# 可写函数说明
def print_me(str_me):
    """打印任何传入的字符串"""
    print(str_me)
    return


# 调用print_me函数
print_me(str_me="菜鸟教程")


# 可写函数说明
# 默认参数：调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
def print_info(name, age=35):
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用print_info函数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
print_info(age=50, name="runoob")
print("------------------------")
print_info(name="runoob")
