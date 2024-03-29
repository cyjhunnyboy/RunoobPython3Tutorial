# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数据结构
        列表
            Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
            一句话概括即：列表可以修改，而字符串和元组不能。
            list.append(x)：把一个元素添加到列表的结尾，相当于a[len(a):]=[x]
            list.extend(L)：通过添加指定列表的所有元素来扩充列表，相当于a[len(a):]=L
            list.insert(i, x)：在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
                               例如a.insert(0, x)会插入到整个列表之前，而a.insert(len(a), x)相当于a.append(x)。
            list.remove(x)：删除列表中值为x的第一个元素。如果没有这样的元素，就会返回一个错误。
            list.pop([i])：从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。
                           元素随即从列表中被移除。（方法中i两边的方括号表示这个参数是可选的，
                           而不是要求你输入一对方括号，你会经常在Python库参考手册中遇到这样的标记。）
            list.clear()：移除列表中的所有项，等于del a[:]。
            list.index(x)：返回列表中第一个值为x的元素的索引。如果没有匹配的元素就会返回一个错误。
            list.count(x)：返回x在列表中出现的次数。
            list.sort()：对列表中的元素进行排序。
            list.reverse()：倒排列表中的元素。
            list.copy()：返回列表的浅复制，等于a[:]。

            注意：类似insert, remove或sort等修改列表的方法没有返回值。
"""
if __name__ == "__main__":
    a = [66.25, 333, 333, 1, 1234.5]

    # 返回x在列表中出现的次数
    print(a.count(333), a.count(66.25), a.count('x'))

    # 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如a.insert(0, x)
    # 会插入到整个列表之前，而a.insert(len(a), x) 相当于a.append(x)
    a.insert(2, -1)

    # 把一个元素添加到列表的结尾，相当于a[len(a):] = [x]
    a.append(333)
    print(a)

    # 返回列表中第一个值为x的元素的索引。如果没有匹配的元素就会返回一个错误
    print(a.index(333))

    # 删除列表中值为x的第一个元素。如果没有这样的元素，就会返回一个错误
    a.remove(333)
    print(a)

    # 倒排列表中的元素
    a.reverse()
    print(a)

    # 对列表中的元素进行排序
    a.sort()
    print(a)
