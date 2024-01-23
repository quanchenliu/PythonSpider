"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/23
 @Function  : Cookie的获取、保存和利用
"""

import http.cookiejar
import urllib.request

'''1、获取网页的Cookie'''
cookie = http.cookiejar.CookieJar()                     # 声明一个 CookieJar 对象
handler = urllib.request.HTTPCookieProcessor(cookie)    # 利用 HTTPCookieProcessor 构建一个 Handler
opener = urllib.request.build_opener(handler)           # 利用 build_opener 构建 Opener
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)


'''2、读取 Cookie 并保存'''
filename = 'cookie.txt'                                 # Cookie 文件路径
# MozillaCookieJar 用于管理和保存 HTTP 请求和响应中的 Cookie 信息
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)          # LWPCookieJar 同样可以读取和保存 Cookie文件，只是文件的格式为 LWP 格式
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response1 = opener.open('https://www.baidu.com')
# ignore_discard 和 ignore_expires 参数表示即使 Cookie 将要被丢弃或已过期，也将其保存。
cookie.save(ignore_discard=True, ignore_expires=True)   # 将 Cookie 保存到文件中。


'''3、读取 Cookie 文件并用于爬取网页'''
cookie = http.cookiejar.LWPCookieJar()
# 调用 load 方法来读取本地的 Cookie 文件，获取了 Cookie 的内容（要求首先生成了 LWPCookieJar 格式的 Cookie，并保存成了文件）
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response2 = opener.open('https://www.baidu.com')
print(response2.read().decode('utf-8'))








