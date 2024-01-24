"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : params 字段添加额外信息//调用 json 方法转化结果格式为字符串
"""

import requests
r = requests.get('https://www.httpbin.org/get')
print(r.text)

data = {
    'name': 'germey',
    'age': 25
}
r = requests.get('https://httpbin.org/get', params=data)        # 使用 params 参数完成附件额外信息
print(r.text, type(r.text))                                     # 网页的返回类型虽然是 str 类型，但却是 json 格式
print(r.json())                                                 # 调用 json 方法，将返回结果转化为字典

