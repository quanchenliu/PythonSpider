"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/9
 @Function  : 百度爬虫广告过滤系统（XPath版）
"""
import requests
import time
import os
import pandas as pd     # 保存csv数据
import re               # 数据清洗

page = 2
keyword = '新疆棉'
params = {
    'category_id':'',
    'search_type': 'video',
    'ad_resource': '5654',
    '__refresh__': 'true',
    '_extra': '',
    'context': '',
    'page': page,
    'page_size': 42,
    'from_source': '',
    'from_spmid': '333.337',
    'platform': 'pc',
    'highlight': '1',
    'single_column': '0',
    'keyword': keyword,
    'qv_id': 'IcRTzIVNdRS8mSCscibyXk9uj63B6Ftr',
    'source_tag': '3',
    'gaia_vtoken': '',
    'dynamic_offset': 24,
    'web_location': '1430654',
    'w_rid': '338307752ecfe4d4f7bf44d755dfd54f',
    'wts': '1710061561',
}




