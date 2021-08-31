# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基本数据类型
        1、List（列表）
            List内置了有很多方法，例如append()、pop()等。

            Python列表截取可以接收第三个参数，参数的作用是截取的步长，
            以下实例在索引1到索引4的位置并设置步长为2（间隔一个位置）来截取字符串
            如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串

            注意：
            1、List写在方括号之间，元素用逗号隔开。
            2、和字符串一样，List可以被索引和切片。
            3、List可以使用+操作符进行拼接。
            4、List中的元素是可以改变的。
'''


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2，而-1表示最后一个元素 list[-1]=4 (与list[3]=4一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数-1表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
