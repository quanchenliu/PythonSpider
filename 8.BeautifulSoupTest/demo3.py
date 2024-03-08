"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/8
 @Function  : BeautifulSoup 的基本用法（方法选择器）
"""
import re

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

# 1、通过 name 参数查询
soup.find_all(name='ul')                        # 查询所有的 ul 节点, 返回的是一个列表
print(type(soup.find_all(name='ul')[0]))        # 列表中的每个元素都是 Tag 类型

for ul in soup.find_all(name='ul'):             # 由于都是 Tag 类型，所有可以执行嵌套查询
    print(ul.find_all(name='li'))               # 查询其内部的 li 节点
    for li in ul.find_all(name='li'):           # 遍历每个 li 节点，以获取其中的文本内容
        print(li.string)

# 2、通过传递属性查询
print(soup.find_all(attrs={'name': 'dromouse'}))        # 得到满足条件的一个列表
print(soup.find_all(attrs={'class': 'title'}))

# 3、通过匹配节点内部的文本查询
# re.compile 使用了正则表达式
print(soup.find_all(text=re.compile('F')))                # 返回的是 所有相匹配文本所组成的列表

# 4、find 方法: 返回第一个匹配的元素
print(soup.find(name='h4'))