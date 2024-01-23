"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/23
 @Function  : 异常处理
"""
import socket
from urllib import request, error


'''1、捕获URLError，并返回错误原因'''
try:
    response = request.urlopen('https://cuiqingcai.com/404')        # 打开一个不存在的页面
except error.URLError as e:
    print(e.reason)


'''2、捕获HTTPError，并返回状态码、原因和请求头'''
try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


'''3、一个在URLError、HTTPError基础上进行优化之后的处理逻辑'''
try:
    response = request.urlopen('https://cuiqingcai.com/404', timeout=0.1)
except error.HTTPError as e:                                        # 先捕获 HTTPError
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:                                         # 再捕获 URLError
    print(e.reason, type(e.reason))                                 # reason 并不总是返回字符串
    if isinstance(e.reason, socket.timeout):                        # 用 isinstance 方法判断错误原因是否是超时
        print('TIME OUT')
else:
    print('Request Successfully')                                   # 最后按照正常逻辑执行

