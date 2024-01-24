"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : 一个正则表达式辅助抓取网页信息的示例
"""

import requests
import re

r = requests.get('https://ssr1.scrape.center/')
# compile用于将正则表达式的字符串模式编译为正则表达式对象;
# re.S 是正则表达式的一个标志，它代表"DOTALL"。在这个模式下，点号 . 匹配任意字符，包括换行符 \n。
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# 使用 re.findall 函数在响应文本 r.text 中查找符合正则表达式 pattern 的所有匹配项，并将匹配到的内容存储在列表 titles 中
titles = re.findall(pattern, r.text)
print(titles)

# ['肖申克的救赎 - The Shawshank Redemption', '霸王别姬 - Farewell My Concubine', '泰坦尼克号 - Titanic', '罗马假日 - Roman Holiday', '这个杀手不太冷 - Léon', '魂断蓝桥 - Waterloo Bridge', '唐伯虎点秋香 - Flirting Scholar', '喜剧之王 - The King of Comedy', '楚门的世界 - The Truman Show', '活着 - To Live']
