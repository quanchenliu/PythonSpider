"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/1
 @Function  : 并发限制（通过信号量机制实现）
"""
import asyncio
import aiohttp

CONCURRENCY = 5                             # 声明爬虫最大并发数: 5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)  # 创建一个信号量对象 semaphore，用于控制最大并发量


async def Scrape_api():
    async with semaphore:                   # 将 semaphore 放入爬取方法中，并使用 async with 语句将 semaphore 作为上下文对象
        print('Scraping: ', URL)
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                await asyncio.sleep(1)
                return await response.text()


async def main():
    scrape_index_tasks = [asyncio.ensure_future(Scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())