"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/11
 @Function  : 查询数据（不使用 fetchall 方法，）
"""
import pymysql

sql = 'SELECT * FROM students WHERE age >= 20'
db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306, db='spiders')
cursor = db.cursor()

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()                 # 通过 while 循环 + fetchone 方法的组合来获取所有数据
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')