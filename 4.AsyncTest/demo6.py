"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/31
 @Function  : 以百度为例测试异步爬虫的效果
"""
import asyncio
import aiohttp
import time

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return response

async def request():
    url = 'https://www.baidu.com/'
    await get(url)


def main():
    for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
        start = time.time()
        tasks = [asyncio.ensure_future(request()) for _ in range(number)]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))

        end = time.time()
        print('Number:', number, 'Cost time:', end - start)


if __name__ == "__main__":
    main()
