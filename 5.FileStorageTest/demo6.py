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


# 将 data 写入 CSV 文件
df = pd.DataFrame(data)                 # 新建一个 DataFrame 对象
df.to_csv('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv', index=False)

# 从 CSV 文件中读取 data
df = pd.read_csv('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.csv')
data = df.values.tolist()               # 调用 .values.tolist 方法，将数据转化为列表
print(data)
for index, row in df.iterrows():        # 对 df 进行逐行遍历，同样能够得到列表类型的结果
    print(row.tolist())