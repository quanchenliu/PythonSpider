"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/23
 @Function  : urlsplit 与 urlunsplit
"""

from urllib.parse import urlsplit
from urllib.parse import urlunsplit

# urlsplit 方法与 urlparse 方法非常类似，但不解析 params 这一部分，只返回 5 个结果
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result, result.scheme, result[0])               # 返回的是一个元组，可以用属性名获取其值，也可以用索引获取

# urlunsplit 方法与 urlunsparse 方法非常类似, 要求参数必须是可迭代的对象（列表、元组等），且长度必须为5
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))



