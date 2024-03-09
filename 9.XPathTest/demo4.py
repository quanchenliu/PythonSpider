"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : XPath 的常见定位方式
"""

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

result = html.xpath('//li[1]/ancestor::*')              # 第一个 li 节点的所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div')            # 第一个 li 节点的 div 祖先节点
print(result)
result = html.xpath('//li[1]/attribute::*')             # 获取第一个 li 节点的所有属性值
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')     # 获取第一个 li 节点的 href 属性为 link1.html 的 a 节点
print(result)
result = html.xpath('//li[1]/descendant::span')                 # 获取第一个 li 节点的 span 子孙节点
print(result)
result = html.xpath('//li[1]/following::*[2]/@href')            # 获取第一个 li 节点的后续所有节点，有索引限制，故只获取第二个 li 节点
print(result)
result = html.xpath('//li[1]/following-sibling::*/a/text()')    # 获取第一个 li 节点之后的所有同级节点
print(result)


























