"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/22
 @Function  : 通过构造 Request 类型的对象，使得更加灵活和丰富地配置参数
"""

import urllib.request
from urllib import parse

'''1、一个简单的 Request 类的用法示例'''
request = urllib.request.Request('https://python.org')      # 构造一个 Request 类型的对象 request
response = urllib.request.urlopen(request)                  # 仍然使用 urlopen 方法，但参数不再是 url，而是 Request 类型的对象
print(response.read().decode('utf-8'))




'''2、传入多个参数构建 Request 类，具体的构建方法见《Python3 网络爬虫开发实战》 33页'''
url = 'https://httpbin.org/post'                                        # url 是必传参数
dict = {'name': 'germey'}                                               # data 部分必须是 bytes 类型
data = bytes(parse.urlencode(dict), encoding='utf-8')
headers = {                                                             # headers 最常用的方法就是添加用户代理 User-Agent
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))





