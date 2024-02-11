"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/11
 @Function  : 使用动态 SQL 语句完成数据插入(通用的插入方法 出现重复信息会发生报错）
"""
import pymysql

data = {
    'id': '20120002',
    'name': 'John',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())               # 将字典 data 中的键(即数据库表的列名)以逗号分隔的形式拼接成一个字符串。
values = ', '.join(['%s'] * len(data))      # 生成一个包含多个 %s 占位符的字符串，用于构建 SQL 语句中的值部分

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    if cursor.execute(sql, tuple(data.values())):       # tuple(data.values()) 的作用是将字典 data 中的值转换为元组。
        print('Successful')
        db.commit()
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
