"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : XPath 如何加载 html 文件
"""

from lxml import etree

def read_method2():
    """通过 etree.parse 方法直接读取文件，显然比先读入到一个字符变量中更加便捷"""
    html = etree.parse('test.html', etree.HTMLParser())
    result = etree.tostring(html)
    print(result.decode('utf-8'))

def read_method1():
    with open('test.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    """etree.HTML 只能处理字符串，而不能直接处理文件对象，因此先将文件读入到 html_content 中"""
    html = etree.HTML(html_content)         # etree 模块可以自动修正 HTML 文本
    result = etree.tostring(html)           # 调用 tostring 即可输出修正后的 HTML 代码，但结果是 bytes 类型
    print(result.decode('utf-8'))           # 调用 decode 方法将其转换成 str 类型

if __name__ == "__main__":
    read_method1()
    read_method2()