# -*- coding: UTF-8 -*-
# author: chenyongjun
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "3.1415926", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('John', 'Smith', 20, 'M', 5000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except pymysql.Error:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
