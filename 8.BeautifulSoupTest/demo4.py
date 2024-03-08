"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/8
 @Function  : BeautifulSoup 的基本用法（CSS选择器）
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('practice_BeautifulSoup.html'), 'lxml')

# 1、直接根据标签名选择节点
items = soup.select('title')
for item in items:
    print(item.string)


# 2、根据 id 选择节点: 在 id 前加 # 号，即可选择该标签
items = soup.select('#s-top-left')          # 选取 id 为 s-top-left 的节点
print(items)
items = soup.select('div#s-top-left')       # 选择 id 为 s-top-left 的 div 节点
print(items)
print('/////////////////////////////////////////////////////////////////////////////////////')


# 3、根据属性选择标签: 在属性值前面加 . 作为 select 的参数, 即可选中所有符合条件的标签
items = soup.select('a.mnav1')          # 选择属性值为 mnav1 的 a 标签
for item in items:
    print(item)                         # 每一个 a 标签
    print(item.string)                  # 标签文本信息
    print(item.attrs)                   # 标签所有的属性
    print(item.get('class'))            # 获取指定属性值
print('/////////////////////////////////////////////////////////////////////////////////////')


# 4、递进式选择标签：父子、子孙关系的节点
items = soup.select('#wrapper > div > a')       # 具有直接父子关系的标签使用 ‘>’，返回的是一个列表
for item in items:
    print(item)
print('\n')

items = soup.select('body li span')             # 不具有直接父子关系的标签使用空格表示，返回的是一个列表
for item in items:
    print(item)
print('\n')
print('/////////////////////////////////////////////////////////////////////////////////////')


# 5、选择具有指定属性的标签
items = soup.select('[href]')                   # 选择具有 href 属性的节点，返回的是一个列表
for item in items:
    print(item)
print('\n')

items = soup.select('a[href]')                  # 选择具有 href 属性的 a 标签，返回的是一个列表
for item in items:
    print(item)
print('\n')

items = soup.select('a[href^="https"]')         # 选择 href 属性值以 https 开头的 a 标签
for item in items:
    print(item)
print('\n')

items = soup.select('a[href$="hao123.com"]')    # 选择以 hao123.com 结尾的 a 标签
for item in items:
    print(item)
print('\n')

items = soup.select('a[href*="www"]')           # 选择 href 属性包含 www 的 a 标签
for item in items:
    print(item)
print('\n')

items = soup.select('div#s-top-left, ul#hotsearch-content-wrapper')     # 同时选取多个标签，返回的是一个列表
for item in items:
    print(item)
print('\n')

items = soup.select('[href="https://haokan.baidu.com/?sfrom=baidu-top"]')  # 根据具体的属性值选择标签
for item in items:
    print(item)
