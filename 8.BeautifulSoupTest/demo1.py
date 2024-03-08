"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/8
 @Function  : BeautifulSoup 的基本用法（提取信息）
"""

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
# 第一个参数是一个 HTML 字符串（但并不完整）
# 第二个参数是解析器类型: lxml
soup = BeautifulSoup(html, 'lxml')          # 定义并初始化一个 BeautifulSoup 对象

# 1、prettify() 方法: 可以将不标准的字符串以标准格式输出（自动更正格式的过程是在初始化BeautifulSoup的时候完成的）
print(soup.prettify())
print('\n', '//////////////////////////////////////////////////////////////')


# 2、输出 title 结点的文本内容: 先选出 title 节点，然后调用 string 属性获取文本内容
print('title is: ', soup.title.string)
print('\n', '//////////////////////////////////////////////////////////////')


# 3、节点选择器: 直接调用节点的名称即可选择节点
print(soup.title, soup.head)
print(soup.p)                               # 仅选择第一个匹配的节点
print('\n', '//////////////////////////////////////////////////////////////')


# 4、提取信息: 通过节点选择器选择节点，以下介绍如何获取节点属性的值
print(soup.p.attrs)                                     # attrs 属性: 获取节点所有属性，返回的是一个字典，通过属性名访问即可
print(soup.p.attrs['name'], soup.p['name'])             # 不使用 attrs，直接传入属性名，此时需要注意返回结果的数据类型
print(soup.p.string)                                    # string 属性: 获取节点中的文本信息
print('\n', '//////////////////////////////////////////////////////////////')


# 5、嵌套选择
print(soup.head, soup.head.title)
print(type(soup.head) == type(soup.head.title))         # 在 Tag 类型的基础上进一步进行选择，得到的仍然是 Tag 类型
print('\n', '//////////////////////////////////////////////////////////////')


# 6、通过 find_all 函数，并传递属性，进行查询
print(soup.find_all(attrs={'name': 'dromouse'}))        # 得到满足条件的一个列表
print(soup.find_all(attrs={'class': 'title'}))