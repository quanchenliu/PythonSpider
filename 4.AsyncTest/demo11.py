"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/1
 @Function  : 超时设置（ClientTimeout）
"""
import aiohttp
import asyncio


async def main():
    timeout = aiohttp.ClientTimeout(total=0.1)                      # 设置超时时间为 1s
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get('https://httpbin.org/get') as response:
                print('status:', response.status)
    except Exception as e:
        print('Error: ', repr(e))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())