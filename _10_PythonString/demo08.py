# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        f-string
            f-string是Python3.6之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法
            f-string格式化字符串以f开头，后面跟着字符串，字符串中的表达式用大括号{}包起来，它会将变量或表达式计算后的值替换进去
            在Python3.8的版本中可以使用=符号来拼接运算表达式与结果

        Unicode 字符串
            在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。
            使用的语法是在字符串前面加上前缀u。
            在Python3中，所有的字符串都是Unicode字符串。
"""
if __name__ == "__main__":
    # 之前我们习惯用百分号(%)
    name = "Runoob"
    print("Hello %s" % name)

    # 替换变量
    print(f"Hello {name}")
    # 使用表达式
    print(f"{1 + 2}")
    word = {"name": "Runoob", "url": "www.runoob.com"}
    print(f"{word['name']}：{word['url']}")
    # Python 3.6
    x = 1
    print(f"{x + 1}")
    # Python 3.8
    print(f"{x + 1 =}")

    # 在Python3中，所有的字符串都是Unicode字符串。
    print(u"你好，我叫Python!")
