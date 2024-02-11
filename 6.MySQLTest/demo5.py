"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/11
 @Function  : 更新数据库（若数据重复，则更新；否则，插入数据库）
"""
import pymysql

data = {
    'id': '20120003',
    'name': 'Jack',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
update = ','.join(["{key} = %s".format(key=key) for key in data])

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306, db='spiders')
cursor = db.cursor()

# ON DUPLICATE KEY UPDATE: 若主键已经存在，就执行更新操作
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# 此时，完整的 SQL 语句为: INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s
sql += update

try:
    if cursor.execute(sql, tuple(data.values())*2):         # 在完整的 SQL 语句中有6个 %s 语句，因此 execute 方法中第二个参数就需要 *2
        print('Successful')
        db.commit()
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
