"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/8
 @Function  : 连接本地数据库的示例
"""
import pymysql

db = pymysql.connect(host='localhost', user='root', password='190901sjnh', port=3306)
cursor = db.cursor()                            # 创建游标对象 cursor，用于执行 SQL 查询和操作。
cursor.execute("CREATE DATABASE students DEFAULT CHARACTER SET utf8mb4")    # 创建一个名为 "students" 的数据库，并使用 utf-8 编码
db.close()                                      # 关闭数据库链接