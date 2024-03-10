"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/10
 @Function  : b 站评论爬虫(TXT版)
"""
import requests
import time
from bs4 import BeautifulSoup
import json


"""获取网页的 HTML 文件"""
def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息

    r = requests.get(url, timeout=30, headers=headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text

"""分析网页文件，整理信息，保存在列表变量中"""
def get_content(url):
    comments = []
    html = get_html(url)                                        # 获取所爬取网页的 HTML 文件
    try:
        s = json.loads(html)                                    # 将 str 类型的 html 转为 字典类型的 s
    except:
        print("json load error")

    num = len(s['data']['replies'])                             # 获取每页评论栏的数量
    # print(num)
    i = 0
    while i < num:
        comment = s['data']['replies'][i]                       # 获取每栏评论
        InfoDict = {                                            # 存储每组信息字典
            'Uname': comment['member']['uname'],                # 用户名
            'Like': comment['like'],                            # 点赞数
            'Content': comment['content']['message'],           # 评论内容
            'Time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))
        }
        comments.append(InfoDict)
        i = i + 1
    return comments


"""将爬取到的文件写入到本地, 保存到当前目录的 BiliBiliComments.txt文件中。"""
def FileStorage(dict):
    with open('BiliBiliComments.txt', 'a+', encoding='utf-8') as f:
        i = 0
        for comment in dict:
            i = i + 1
            try:
                f.write('姓名：{}\t  点赞数：{}\t \n 评论内容：{}\t  评论时间：{}\t \n '.format(
                    comment['Uname'], comment['Like'], comment['Content'], comment['Time']))
                f.write("-----------------\n")
            except:
                print("out2File error")
        print('当前页面保存完成')


if __name__ == '__main__':
    e = 0
    page = 1
    while e == 0:
        url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + "&type=1&oid=455803935&sort=2"
        print(url)
        try:
            content = get_content(url)
            print("page:", page)
            FileStorage(content)
            page = page + 1

            # 为了降低被封 ip 的风险，每爬 10 页便歇 5 秒。
            if page % 10 == 0:
                time.sleep(5)
        except:
            e = 1
