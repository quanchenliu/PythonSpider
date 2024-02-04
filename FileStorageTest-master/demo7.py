"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : CSV 文件的读取
"""
import csv

with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)            # reader 是一个 Reader 对象
    for row in reader:                      # 遍历输出每一行，每一行都是一个列表
        print(row)
