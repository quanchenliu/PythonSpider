"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : 爬取网页数据，并以 .txt 格式存储（open、write、close）
"""
import pymysql


id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root',
                     password=None, port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
    print('Insert successfully')
except:
    db.rollback()
db.close()
