# -*- coding: UTF-8 -*-
# author: chenyongjun
import pymysql

"""
数据库查询操作
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
"""

# 打开数据库连接
db = pymysql.connect("localhost", "root", "3.1415926", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % 1000
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("first_name=%s, last_name=%s, age=%d, sex=%s, income=%d" % \
 \
              (first_name, last_name, age, sex, income))
except pymysql.Error:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
