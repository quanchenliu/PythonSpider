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
# 这种写法可以有效避免字符串拼接的麻烦和引号冲突的问题
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))    # 通过元组的方式进行数据传递
    db.commit()                             # 在执行写操作（如 INSERT、UPDATE、DELETE）后，都需要调用 commit() 方法将事务提交，才能使修改生效
    print('Insert successfully')
except:
    db.rollback()                           # 若执行失败，则调用 rollback 执行数据回滚
db.close()

'''数据回滚是数据库事务处理中的一种重要机制，它用于撤销之前已经执行但尚未提交的事务操作，将数据库恢复到之前的状态。'''