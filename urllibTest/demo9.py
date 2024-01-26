"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/24
 @Function  : robotparser 模块中 RobotFileParser 类的使用
"""

from urllib.robotparser import RobotFileParser

'''1、构造方法1：先声明RobotFileParser 类，然后使用 set_url 设置 robots.txt 文件的路径'''
rp = RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()

'''2、构造方法2：在构造时直接传入robots.txt 文件的路径'''
rp1 = RobotFileParser('https://www.baidu.com/robots.txt')
rp1.read()

'''3、检查 User-Agent 对应的搜索引擎是否能够完成指定 URL 的抓取'''
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com'))


























