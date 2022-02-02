# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数据结构
        将列表当做堆栈使用
            列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
            最先进入的元素最后一个被释放（后进先出）。用 append()
            方法可以把一个元素添加到堆栈顶。用不指定索引的pop()方法可以把一个元素从堆栈顶释放出来

            list.append(x)：把一个元素添加到列表的结尾，相当于a[len(a):] = [x]
             list.pop([i])：从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。
                           元素随即从列表中被移除。（方法中i两边的方括号表示这个参数是可选的，
                           而不是要求你输入一对方括号，你会经常在Python库参考手册中遇到这样的标记。）
"""
if __name__ == "__main__":
    stack = [3, 4, 5]

    stack.append(6)
    stack.append(7)
    print(stack)

    stack.pop()
    print(stack)

    stack.pop()
    print(stack)
