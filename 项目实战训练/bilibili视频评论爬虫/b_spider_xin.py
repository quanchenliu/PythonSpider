"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : 百度爬虫广告过滤系统（XPath版）
"""
import requests
import json
import time
import pandas as pd

"""
  功能：访问 url 的网页，获取网页内容并返回
  参数：目标网页的 url
  返回：目标网页的 html 内容
  """
def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.url)
        return r.text
    except requests.HTTPError or requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")

"""
    功能：根据参数 html 给定的内存型 HTML 文件，尝试解析其结构，获取所需内容
    参数：html, 类似文件的内存 HTML 文本对象
"""
def get_content(html):
    try:
        s = json.loads(html)            # 将 str 类型的 html 转为 字典类型的 s
    except:
        print("json load error")

    num = len(s['data']['replies'])     # 获取每页评论栏的数量

    comments = []                       # 存储每栏评论的字典
    hlist = ["名字", "性别",  "评论", "点赞数", "回复数", "时间"]  #

    i = 0
    while i < num:
        comment = s['data']['replies'][i]           # 获取每栏评论
        blist = []                                  # 存储每组信息的字典

        username = comment['member']['uname']       # 用户名
        sex = comment['member']['sex']              # 性别
        content = comment['content']['message']     # 评论内容
        likes = comment['like']                     # 点赞数
        rcounts = comment['rcount']                 # 回复数
        ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))  # 发布时间

        blist.append(username)
        blist.append(sex)
        blist.append(ctime)
        blist.append(content)
        blist.append(likes)
        blist.append(rcounts)

        comments.append(blist)
        i = i + 1
    return comments


"""功能：将所获得的数据字典写入到本地文本中"""
def writePage(comments):
    dataframe = pd.DataFrame(comments)   # dataframe为带标签的二维数组
    print(dataframe)

    # a:只能写, 可以不存在, 必不能修改原有内容, 只能在结尾追加写, 文件指针无效
    # 不包含索引, 分隔符为逗号, 不包含列名
    dataframe.to_csv('Bilibili_xinjiangmian_comment.csv', mode='a', index=False, sep=',', header=False, encoding='utf-8')

if __name__ == '__main__':
    e = 0
    page = 1
    while e == 0:
        url ='https://api.bilibili.com/x/v2/reply?type=1&oid=336260172&pn=' + str(page)
        print(page, url)
        try:
            html = get_html(url)
            comment = get_content(html)
            writePage(comment)
            page = page + 1
            # 为了降低被封 ip 的风险，每爬 20 页便歇 5 秒。
            if page % 10 == 0:
                time.sleep(5)
        except:
            e = 1