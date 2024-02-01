"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/31
 @Function  : 一个基本的 aiohttp 案例
"""
import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text(), response.status


async def main():
    url = 'https://cuiqingcai.com'
    html, status = await get(url)
    print(f'html: {html[:100]}...')
    print(f'status: {status}')


if __name__ == '__main__':
    asyncio.run(main())                 # 总会出现 RuntimeError: Event loop is closed 的错误
    ''' 一种可行的解决方案是将 asyncio.run(协程主函数名())修改为：
        loop = asyncio.get_event_loop()
        loop.run_until_complete(协程主函数名())
    '''
