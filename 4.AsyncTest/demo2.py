"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/30
 @Function  : 协程的用法（event_loop、coroutine、task（create_task）、task（ensure_future））
"""
import asyncio

async def execute(x):
    print('Number:', x)

def main():
    # 有三种创建 task 对象的方法：create_task(显式) 和 ensure_future(显式)、直接调用run_until_complete方法(隐式)
    method = {'MODE': 'ensure_future'}
    coroutine = execute(1)                          # 调用 execute 方法，但并不执行，而是返回一个 coroutine 协程对象
    print('Coroutine:', coroutine)                  # Coroutine: <coroutine object execute at 0x000001E2BD4C26C0>

    if method['MODE'] == 'Notask':
        # 创建一个事件循环 loop, 调用 loop 对象的 run_until_complete 方法，将协程对象注册到了事件循环中，并执行 execute 方法
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coroutine)          # Number: 1

    if method['MODE'] == 'create_task':
        loop = asyncio.get_event_loop()
        task = loop.create_task(coroutine)
        # print('Task:', task)
        loop.run_until_complete(task)               # 等价于: loop.run_until_complete(coroutine)
        # print('Task:', task)

    if method['MODE'] == 'ensure_future':
        # 使用 ensure_future 方法创建 task 对象————即使还没有声明 loop 也可以提前定义好 task 对象
        task = asyncio.ensure_future(coroutine)
        # print('Task:', task)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(task)
        # print('Task:', task)


if __name__ == "__main__":
    main()
