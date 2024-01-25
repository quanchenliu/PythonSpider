"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/23
 @Function  : 引入一些高级用法（Handler类），本例尝试爬取一个具有用户登陆验证的网页
"""

from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler                 # 用于解决代理问题
from urllib.request import build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://static3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()               # 创建一个 HTTPPasswordMgrWithDefaultRealm 对象
p.add_password(None, url, username, password)       # 添加url、用户名、密码
auth_handler = HTTPBasicAuthHandler(p)              # 实例化一个 HTTPBasicAuthHandler 对象 auth_handler
opener = build_opener(auth_handler)                 # 利用 Opener 类中的 open 方法打开链接，即可完成验证

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
