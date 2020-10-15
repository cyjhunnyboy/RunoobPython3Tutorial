# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
List（列表）
    List（列表）是Python中使用最频繁的数据类型。
    列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
    列表是写在方括号[]之间，用逗号分隔开的元素列表。
    和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
    列表截取的语法格式如下：
    变量[头下标:尾下标]

    List内置了有很多方法，例如append()、pop()等。

    注意：
    1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，List可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。
'''


def reverse_words(input_word):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    input_words = input_word.split(" ")

    # 翻转字符串
    # 假设列表list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而-1表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # input_words[-1::-1] 有三个参数
    # 第一个参数-1表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1表示逆向
    input_words = input_words[-1::-1]

    # 重新组合字符串
    output_words = ' '.join(input_words)

    return output_words


if __name__ == "__main__":
    t = ["a", "b", "c", "d", "e"]
    print(t[1:3])
    print(t[:4])
    print(t[3:])
    print(t[:])

    list_a = ['abcd', 786, 2.23, 'runoob', 70.2]
    tiny_list = [123, 'runoob']

    # 输出完整列表
    print(list_a)
    # 输出列表第一个元素
    print(list_a[0])
    # 从第二个开始输出到第三个元素
    print(list_a[1:3])
    # 输出从第三个元素开始的所有元素
    print(list_a[2:])

    # 星号*是重复操作
    # 输出两次列表
    print(tiny_list * 2)

    # 加号+是列表连接运算符
    # 连接列表
    print(list_a + tiny_list)

    # 与Python字符串不一样的是，列表中的元素是可以改变的：
    a = [1, 2, 3, 4, 5, 6]
    a[0] = 9
    a[2:5] = [13, 14, 15]
    print(a)
    # 将对应的元素值设置为[]
    a[2:5] = []
    print(a)

    # Python列表截取可以接收第三个参数，参数作用是截取的步长，
    # 以下实例在索引1到索引4的位置并设置为步长为2（间隔一个位置）来截取字符串
    letters = ["c", "h", "e", "c", "k", "i", "o"]
    print(letters[1:4:2])

    # 翻转字符串
    reverse_word = 'I like runoob'
    reverse_word = reverse_words(reverse_word)
    print(reverse_word)
