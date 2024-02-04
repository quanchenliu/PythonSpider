"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/4
 @Function  : 爬取网页数据，并以 .txt 格式存储（open、write、close）
"""
import requests
from pyquery import PyQuery as pq
import re

url = 'https://static1.scrape.center/'
html = requests.get(url).text                       # 获取网站首页的 HTML 代码
doc = pq(html)                                      # 利用 pyquery 解析库将电影的名称、类别、上映时间、评分等信息提取出来
items = doc('.el-card').items()

with open('movies.txt', 'w', encoding='utf-8') as file:
    for item in items:
        # 名称
        name = item.find('a > h2').text()
        file.write(f'名称: {name}\n')
        # 类别
        categories = [item.text() for item in item.find('.categories button span').items()]
        file.write(f'类别: {categories}\n')
        # 上映时间
        published_at = item.find('.info:contains(上映)').text()
        published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
            if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
        file.write(f'上映时间: {published_at}\n')
        # 评分
        score = item.find('p.score').text()
        file.write(f'评分: {score}\n')
        file.write(f'{"=" * 50}\n')