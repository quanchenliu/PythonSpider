"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/1
 @Function  : aiohttp 还支持其他请求类型———— POST、PUT、DELETE，下面以 POST 为例，其余请求类型发使用与之相同
"""
import aiohttp
import asyncio

async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
































