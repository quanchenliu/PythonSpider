"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : XPath 如何选取节点
"""

from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())

# 以下的提取结果均为一个列表，其中元素的类型为 element
result = html.xpath('//*')              # 选取所有节点，* 表示匹配所有节点
print(result)

result = html.xpath('//li')             # 选取所有名为 li 的节点
print(result)

result = html.xpath('//li/a')           # 选取所有 li 节点的所有直接子节点 a
print(result)

result = html.xpath('//ul//a')          # 选取所有 ul 节点的子孙节点 a, 注意此处不能使用'//ul/a'
print(result)

# 选取 a 节点中 href 属性为 link4.html 的节点，并获取其父节点的 class 属性
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 另一种选取父节点的方法，通过 parent:: 获取父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)




















