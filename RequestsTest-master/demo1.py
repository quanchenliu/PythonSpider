"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : requests 库的 get 方法（与 urllib 库中的 urlopen 方法对应）
"""
import requests

'''1、get 方法'''
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(r.cookies)
print(r.text[:100])
print(type(r.text))

'''2、POST、PUT、DELETE、PATCH'''
r = requests.post('https://www.httpbin.org/post')
r1 = requests.put('https://www.httpbin.org/put')
r2 = requests.delete('https://www.httpbin.org/delete')
r3 = requests.patch('https://www.httpbin.org/patch')