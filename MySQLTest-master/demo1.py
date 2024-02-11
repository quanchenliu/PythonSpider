"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/8
 @Function  : 连接本地数据库的示例
"""
import pymysql

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306)
cursor = db.cursor()                            # 创建游标对象 cursor，用于执行 SQL 查询和操作。
cursor.execute('SELECT VERSION()')              # 执行 SQL 查询语句
data = cursor.fetchone()                        # 从查询结果中获取版本信息
print('Database version:', data)

# 创建一个名为 "spiders" 的数据库，并使用 utf-8 编码
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
db.close()                                      # 关闭数据库链接
