# -*- coding: UTF-8 -*-
# author: chenyongjun
from urllib.request import urlopen

"""
访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request
以及用于发送电子邮件的 smtplib
"""

for line in urlopen('https://www.baidu.com'):
    line = line.decode("utf-8")  # Decoding the binary data to text.
    if 'baidu' in line or 'www.baidu.com' in line:  # look for Eastern Time
        print(line)
