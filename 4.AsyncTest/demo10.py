"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/2/1
 @Function  : 获取响应的状态码、响应头、响应体、响应体二进制内容、响应体 JSON 结果
"""
import aiohttp
import asyncio


async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print('status:', response.status)                   # 状态码
            print('headers:', response.headers)                 # 响应头
            print('body:', await response.text())               # 响应体
            print('bytes:', await response.read())              # 响应体二进制内容
            print('json:', await response.json())               # 响应体 JSON 结果


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())























