"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : 利用 pandas 库对 CSV 文件进行读取或写入
"""
import pandas as pd

data = [
    {'id': '10001', 'name': 'Mike', 'age': 20},
    {'id': '10002', 'name': 'Bob', 'age': 22},
    {'id': '10003', 'name': 'Jordan', 'age': 21},
]

df = pd.DataFrame(data)         # 新建一个 DataFrame 对象
df.to_csv('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', index=False)