# -*- coding: UTF-8 -*-
# author: chenyongjun

""""
列表推导式
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，
或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if
上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号
"""
vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])

fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in fresh_fruit])

print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
"""
嵌套列表解析
Python的列表还可以嵌套。
以下实例展示了3X4的矩阵列表
"""
matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

"""
del 语句
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
