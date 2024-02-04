"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/3
 @Function  : Ajax + 异步爬虫 + json存储
"""
import asyncio
import json
import time
import aiohttp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 18
TOTAL_PAGE = 11
COUNTER = 5
semaphore = asyncio.Semaphore(COUNTER)
session = None
RESULTS_DIR = 'C:/Users/DELL/Desktop/python爬虫基础/3.AjaxTest/data'

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

async def Scrape_api(url):
    async with semaphore:
        try:
            logging.info('Scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('Error occurred while scraping %s', url, exc_info=True)

async def Scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return await Scrape_api(url)

async def Scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await Scrape_api(url)
    await save_data(data)

async def main():
    start = time.time()

    global session
    session = aiohttp.ClientSession()

    # 爬取列表页的数据
    scrape_index_tasks = [asyncio.ensure_future(Scrape_index(page)) for page in range(1, TOTAL_PAGE + 1)]
    results = await asyncio.gather(*scrape_index_tasks)

    # 获取每部电影的id
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))

    # 根据id，爬取电影详情页的数据
    scrape_detial_tasks = [asyncio.ensure_future(Scrape_detail(id)) for id in ids]
    await asyncio.gather(*scrape_detial_tasks)
    await session.close()

    end = time.time()
    print('Using time:', end - start)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
