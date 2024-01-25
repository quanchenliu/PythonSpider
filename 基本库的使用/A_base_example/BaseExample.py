"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/22
 @Function  : 一个基本的爬虫实战案例
"""
import json
import multiprocessing
import re
import requests
import logging
from urllib.parse import urljoin
from os.path import exists
from os import makedirs

TOTAL_PAGE = 10
BASE_URL = 'https://ssr1.scrape.center'
RESULT_DIR = 'C:/Users/DELL/Desktop/python爬虫基础/基本库的使用/A_base_example'
# 将日志级别设置为 INFO，这意味着将记录 INFO 及更高级别的日志消息。
# %(asctime)s: 记录日志的时间。 %(levelname)s: 日志消息的级别。 %(message)s: 日志消息的主体内容
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')

# 定义爬取页面的方法
def scrape_page(url):
    logging.info('Scraping %s ...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text                # 返回 HTML 代码
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)        # 否则输出错误信息
    except requests.RequestException:           # 爬取过程中出现异常，执行 except 代码段
        logging.error('error occured while scraping %s', url, exc_info=True)

# 定义列表页的URL拼接方法并完成页面 html 代码的获取
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

# 解析列表页，并得到详情页的URL
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name"')        # 定义提取标题的正则表达式
    items = re.findall(pattern, html)                               # 提取列表页所有的匹配的值
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url                                            # 调用 yield 方法，用于产生一个值，并暂停生成器的执行，直到下一次调用

# 获取详情页的 html 代码
def scrape_detail(url):
    return scrape_page(url)

# 解析详情页代码，并得到需要的封面、名称、类别、上映时间、评分、剧情简介(此处的正则表达式可以用 XPath 或者 CSS 选择器来替代）
def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*/)".*?class="cover">', re.S)                   # 封面
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')                                                          # 名称
    categories_pattern = re.compile('<button.*?category.*?<span>(.*/)</span>.*?</button>', re.S)            # 类别
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')                                          # 上映时间
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)                                  # 评分
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)                                             # 剧情简介

    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()) if re.search(score_pattern, html) else None


    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'score': score,
        'drama': drama
    }

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to json file...')
        save_data(data)
        logging.info('data saved successfully')



if __name__ == "__main__":
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE+1)
    pool.map(main, pages)
    pool.close()
    pool.join()
