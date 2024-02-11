"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/11
 @Function  : 查询数据（查询无需 commit 方法）
"""
import pymysql

sql = 'SELECT * FROM students WHERE age >= 20'          # 查询条件

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306, db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)                                 # 执行查询语句
    print('Count:', cursor.rowcount)                    # 调用 count 属性，获取查询结果的条数

    one = cursor.fetchone()                             # 调用 fetchone 方法，获取结果的第一条数据，并以元组形式呈现
    print('One:', one)

    results = cursor.fetchall()                         # 调用 fetchall 方法，获取所有结果，并以二重元组形式呈现
    print('Results:', results)
    print('Results Type:', type(results))

    for row in results:
        print(row)
except:
    print('Error')