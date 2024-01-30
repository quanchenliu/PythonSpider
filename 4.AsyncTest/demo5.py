"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/30
 @Function  : 协程实现
"""
import asyncio
import time
import aiohttp

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response

async def request():
    url = 'https://httpbin.org/delay/5'
    print('Waiting for ', url)
    response = await get(url)           # await 后面可以跟一个协程对象，而不能跟 requests 返回的 Response 对象
    print('Get response from ', url, 'response', response)

def main():
    start = time.time()
    tasks = [asyncio.ensure_future(request()) for _ in range(10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print('Cost time:', end - start)

if __name__ == "__main__":
    main()
