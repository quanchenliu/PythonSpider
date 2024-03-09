"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : 百度爬虫广告过滤系统（XPath版）
"""

import requests
import json
from lxml import etree

key_words = '新疆棉'
# 页面深度
depth = 1
# 伪装浏览器头部
kv = {
    "User-Agent":  "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
}

for i in range(depth):
    url = 'https://www.baidu.com/s?wd=' + key_words + '&pn=' + str(i * 10)
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
    except:
        print('Error2')


    text_html = etree.HTML(html, etree.HTMLParser())

    # 对爬取的内容进行过滤筛选
    r1 = text_html.xpath('//div[@class="result c-container new-pmd"]//h3')  # 获取文字标题
    r2 = text_html.xpath('//*[@class="c-abstract"]')                        # 获取内容简介
    r3 = text_html.xpath('//*[@class="t"]/a/@href')                         # 获取内容链接
    r4 = text_html.xpath('//*[@class="c-abstract"]/span')                   # 获取发布时间
    a = [len(r1), len(r2), len(r3), len(r4)]
    a = min(a)

    for i in range(a):
        # 我们在爬取网站使用Xpath提取数据的时候，最常使用的就是Xpath的text()方法，该方法可以提取当前元素的信息
        # 但是某些元素下包含很多嵌套元素，我们想一并的提取出来，这时候就用到了string(.)方法
        r11 = r1[i].xpath('string(.)')
        r22 = r2[i].xpath('string(.)')
        r33 = r3[i]
        r44 = r4[i].xpath('string(.)')

        # 将爬取到的内容写入‘新疆棉.txt’文件中
        with open('新疆棉.txt', 'a', encoding='utf-8') as c:
            # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            c.write(json.dumps(r11, ensure_ascii=False) + '\n')
            c.write(json.dumps(r22, ensure_ascii=False) + '\n')
            c.write(json.dumps(r33, ensure_ascii=False) + '\n')
            c.write(json.dumps(r44, ensure_ascii=False) + '\n' + '\n')