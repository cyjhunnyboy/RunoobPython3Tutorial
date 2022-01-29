# -*- coding: UTF-8 -*-
# author: chenyongjun
import pymysql

"""
删除操作
删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据
"""

# 打开数据库连接
db = pymysql.connect("localhost", "root", "3.1415926", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = '%s'" % "John"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except pymysql.Error:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
