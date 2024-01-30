"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/1/30
 @Function  : 不使用异步爬虫爬取大规模数据
"""
import requests
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

TOTAL_NUMBER = 100
URL = 'https://httpbin.org/delay/5'

start_time = time.time()
for _ in range(1, TOTAL_NUMBER + 1):
    logging.info('scraping %s', URL)
    response = requests.get(URL)
end_time = time.time()
logging.info('total time %s seconds', end_time - start_time)
