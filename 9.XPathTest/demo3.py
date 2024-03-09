"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : XPath 的常见定位方式
"""

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

# 1、属性唯一: 通过元素属性，快速定位
result = html.xpath('//*[@href="link3.html"]')
print(result)

# 2、没有属性: 属性与层级的结合
result = html.xpath('//li[@class="item-0"]/a')
print(result)

# 3、多个属性重名: 属性与逻辑结合
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

# 4、某一属性具有多个值: contains 方法, (参数名称, 参数值)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# 5、按序选择: 通过索引实现
result1 = html.xpath('//li[1]/a/text()')                 # 选取第一个 li 节点的直接子节点 a
result2 = html.xpath('//li[last()]/a/text()')            # 选取最后一个 li 节点(last())
result3 = html.xpath('//li[position()<3]/a/text()')      # 选择了位置小于 3 的节点
result4 = html.xpath('//li[last()-2]/a/text()')          # 选择了倒数第 3 个节点
print(result1, result2, result3, result4)