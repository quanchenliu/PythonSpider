"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  :CSV 文件写入字典(DictWriter、writeheader、writerow、utf-8-sig格式、newline参数)
"""
import csv

with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    filenames = ['id', 'name', 'age']                               # 定义3个字段并用filenames
    writer = csv.DictWriter(csvfile, fieldnames=filenames)          # 调用 DictWriter 方法初始化一个字典写入对象
    writer.writeheader()                                            # 调用 writeheader 方法写入头信息
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})     # 调用 writerow 方法写入相应字典(自动在行末添加换行符)
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# 若想要追加写入数据，则修改文件打开模式，将‘w’改为‘a’
with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})

# 若要写入中文内容，则需要指定编码格式 'utf-8-sig' 而不是 'utf-8'
with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})