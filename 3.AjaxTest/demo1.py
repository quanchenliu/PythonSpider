"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/2
 @Function  : Ajax + json 存储
"""
import time
import aiohttp
import asyncio
import logging
import json
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'C:/Users/DELL/Desktop/python爬虫基础/3.AjaxTest'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)
CONCURRENCY = 5                             # 声明爬虫最大并发数: 5
semaphore = asyncio.Semaphore(CONCURRENCY)  # 创建一个信号量对象 semaphore，用于控制最大并发量

# 定义爬取方法，该方法专门处理 JSON 接口
async def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
        logging.error('get invalid status code %s while scraping %s', response.status, url)
    except aiohttp.ClientError as e:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 定义爬取列表页的方法
async def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return await scrape_api(url)

# 定义爬取详情页的方法
async def scrape_detail(movie_id):
    url = DETAIL_URL.format(id=movie_id)
    return await scrape_api(url)

# 定义存储数据的方法
async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json_data = {
        "电影名称": name,
        "电影种类": data.get('categories'),
        "制作国家": data.get('regions'),
        "电影评分": data.get('score'),
        "电影时长": data.get('minute'),
        "电影简介": data.get('drama'),
        "上映时间": data.get('published_at')
    }
    json.dump(json_data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

async def Scrape(page):
    index_data = await scrape_index(page)               # 爬取列表页的 Ajax 接口中的数据
    for item in index_data.get('results'):              # 获取 results 字段中的数据
        movie_id = item.get('id')                       # 获取电影的 id
        detail_data = await scrape_detail(movie_id)     # 获取详情页的数据
        await save_data(detail_data)                    # 保存数据

async def main():
    start = time.time()

    tasks = [asyncio.ensure_future(Scrape(page)) for page in range(TOTAL_PAGE+1)]
    await asyncio.gather(*tasks)

    end = time.time()
    print('Use time:', end - start)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
