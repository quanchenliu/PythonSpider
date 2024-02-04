"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : CSV 文件写入列表（writer方法、writerow方法、writerows方法、delimiter参数）
"""
import csv

with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')  # 若要指定列与列之间的分隔符，可以传入 delimiter 参数
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

    # writer = csv.writer(csvfile)                    # CSV 文件默认以逗号为分隔符
    # writer.writerow(['id', 'name', 'age'])          # 调用 writerows 方法同时写入多行，传入参数为二维列表
    # writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
