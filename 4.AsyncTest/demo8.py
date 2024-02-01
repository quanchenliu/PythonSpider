"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/1
 @Function  : 设置 URL 参数
"""
import aiohttp
import asyncio


async def main():
    params = {                      # 对 URL 参数的设置，我们可以借助 params 参数，传入一个字典即可
        'name': 'germey',
        'age': 25
    }
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


