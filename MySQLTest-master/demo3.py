"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/8
 @Function  : 插入数据(插入、删除、更新操作的代码模板)
"""
import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()                     # commit 方法才是将语句提交到数据库执行的方法
    print('Insert successfully')
except:
    db.rollback()                   # 若执行失败，啧调用 rollback 执行数据回滚
db.close()
