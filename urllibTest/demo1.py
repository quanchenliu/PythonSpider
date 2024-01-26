"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/22
 @Function  : urllibTest.request 模块提供了最基本的构造HTTP请求的方法 urlopen
"""

import socket
import urllib.parse
import urllib.request
import urllib.error


'''1、利用 urlopen 方法，完成对简单网页的 GET 请求抓取'''
response = urllib.request.urlopen('https://www.python.org')  # 获取响应，并赋值给 response
print(response.status)                                      # 获取响应的状态码
print(response.getheaders())                                # 获取响应头信息（全部）
print(response.getheader('Server'))                         # 获取响应头信息（部分）
print(type(response))                                       # type 方法得到响应的类型
# print(response.read().decode('utf-8'))                    # read 方法可以得到响应的内容，并规定编码方式


'''2、urlopen 的 data 参数'''
string = urllib.parse.urlencode({'name': 'germey'})         # 使用 urllibTest.parse 模块里的 urlencode 方法将字典参数转化为字符串
data = bytes(string, encoding='utf-8')                      # bytes(字符串，编码格式): 将 str 对应的字符串按 utf-8 格式转换为 bytes 类型
print(type(data))
response = urllib.request.urlopen('https://httpbin.org/post', data=data)                # 传递 data 参数后，请求方式变为 POST
print(response.read().decode('utf-8'))


'''3、urlopen 的 timeout 参数'''
try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)          # 设置超时时间为0.1
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):                # isinstance(obj, class_or_tuple) 用于检查对象 obj 是否是指定类或元组中任意类的实例。
        print('TIME OUT')
print(response.read())
