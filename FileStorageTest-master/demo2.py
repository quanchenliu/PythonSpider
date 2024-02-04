"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : 读取json （open、write、loads、load、get）
"""
import json

with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.json', encoding='utf-8') as file:
    str = file.read()               # 先从 json 文件中读取文本数据, 并存储为字符串 str
    data = json.loads(str)          # 将文本字符串 str 转化为 json 对象
    print(data[0].get('name'))


# 上述示例的更简单用法: 直接用 load 方法传入文件操作对象(注意，是 load 不是 loads)
# data = json.load(open('data.json', encoding='utf-8'))
# print(data)