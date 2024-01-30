"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/30
 @Function  : 多任务协程
"""
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

tasks = [asyncio.ensure_future(request()) for _ in range(5)]    # 定义一个 task 列表
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))                    # 使用 wait 方法执行，从而实现执行多次请求

for task in tasks:
    print('Task Result:', task.result())

