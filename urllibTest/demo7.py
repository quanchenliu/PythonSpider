"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : urlunparse 用于构造 URL
 """
from urllib.parse import urlunparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# urlunparse 要求参数必须是可迭代的对象（列表、元组等），且长度必须为6
print(urlunparse(data))







