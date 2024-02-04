"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : 输出 json（open、write、dumps）
"""
import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
    },
    {
    'name': ' 王伟 ',
    'gender': ' 男 ',
    'birthday': '1992-10-18'
}]

# 调用 dumps 方法将 json 对象转化为字符串
# indent=2 用于保证 json 数据的缩进格式
# ensure_ascii=False 用于保证中文字符的正常输出
with open('C:/Users/DELL/Desktop/python爬虫基础/5.FileStorageTest/data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))

# 同样的，dumps 方法有与之对应的 dump 方法
json.dump(data, open('data.json', 'a', encoding='utf-8'), indent=2, ensure_ascii=False)