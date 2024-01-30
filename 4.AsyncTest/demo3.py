"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/30
 @Function  : 为 task 对象绑定回调方法
"""
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status                   # 请求百度，并获取其状态码

def callback(task):                         # 定义回调方法
    print('Status:', task.result())         # 接收一个 task 参数，并使用 print 打印出了 task 对象的结果

coroutine = request()                       # 创建一个协程对象
task = asyncio.ensure_future(coroutine)     # 将协程对象转换为一个 task 对象
task.add_done_callback(callback)            # 将回调方法传递给封装好的 task 对象，当 task 执行完毕后，就可以调用 callback 方法
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)