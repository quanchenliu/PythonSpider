"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : urlparse 用于对 URL 的识别和分段
"""

from urllib.parse import urlparse

'''1、urlparse 对 URL 的识别和分段'''
# scheme://netloc/path;params?query#fragment
# 协议://域名/访问路径;参数?查询条件#锚点
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')         # 返回一个 Parse Result 类型的对象（其实质是一个字典）
print(type(result), result)
print(result.scheme, result[0])


'''2、urlparse 的三个参数: URL、scheme、allow_fragments'''
# 如果 URL 没有携带协议信息，则使用 scheme 确定的协议
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

# scheme 只有在 URL 没有携带协议信息的时候才生效；allow_fragments 为false，则 fragment 部分会被解析为 path、params、query 的一部分
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', scheme='http', allow_fragments=False)
print(result)

