# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python 三引号
            python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符

            三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的
            一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐

            cursor.execute(\'''
            CREATE TABLE users (
            login VARCHAR(8),
            uid INTEGER,
            prid INTEGER)
            \''')
"""
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

if __name__ == "__main__":
    print(para_str)
    print(errHTML)
