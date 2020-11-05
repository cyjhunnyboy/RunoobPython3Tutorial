# -*- coding: UTF-8 -*-
# author: chenyongjun
import pymysql

"""
创建数据库表
如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE
"""

# 打开数据库连接
db = pymysql.connect("localhost", "root", "3.1415926", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# create schema [数据库名称] default character set utf8 collate utf8_general_ci;--创建数据库
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
