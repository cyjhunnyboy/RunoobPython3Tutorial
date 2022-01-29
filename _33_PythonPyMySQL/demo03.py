# -*- coding: UTF-8 -*-
# author: chenyongjun
import pymysql

"""
数据库插入操作
以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录
"""

# 打开数据库连接
db = pymysql.connect("localhost", "root", "3.1415926", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Candy', 'Sy', 33, 'W', 7000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except pymysql.Error:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
