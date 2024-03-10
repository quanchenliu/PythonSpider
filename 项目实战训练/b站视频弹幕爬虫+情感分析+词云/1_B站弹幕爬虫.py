# 程序功能：爬取B站视频弹幕
# 作者：马哥python说

import re  # 正则表达式提取文本
import requests  # 爬虫发送请求
from bs4 import BeautifulSoup as BS  # 爬虫解析页面
import time
import pandas as pd  # 存入csv文件
import os


def get_bilibili_danmu(v_url, v_result_file):
	"""
	爬取B站弹幕
	:param v_url: 视频地址
	:param v_result_file: 保存文件名
	:return:
	"""
	headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)", }
	print('视频地址是：', v_url)
	r1 = requests.get(url='https://api.bilibili.com/x/player/pagelist?bvid='+bv, headers=headers)
	html1 = r1.json()
	cid = html1['data'][0]['cid']  # 获取视频对应的cid号
	print('该视频的cid是:', cid)
	danmu_url = 'http://comment.bilibili.com/{}.xml'.format(cid)  # 弹幕地址
	print('弹幕地址是：', danmu_url)
	r2 = requests.get(danmu_url)
	html2 = r2.text.encode('raw_unicode_escape')  # 编码格式
	soup = BS(html2, 'xml')
	danmu_list = soup.find_all('d')
	print('共爬取到{}条弹幕'.format(len(danmu_list)))
	video_url_list = []  # 视频地址
	danmu_url_list = []  # 弹幕地址
	time_list = []  # 弹幕时间
	text_list = []  # 弹幕内容
	for d in danmu_list:
		data_split = d['p'].split(',')  # 按逗号分隔
		temp_time = time.localtime(int(data_split[4]))  # 转换时间格式
		danmu_time = time.strftime("%Y-%m-%d %H:%M:%S", temp_time)
		video_url_list.append(v_url)
		danmu_url_list.append(danmu_url)
		time_list.append(danmu_time)
		text_list.append(d.text)
		print('{}:{}'.format(danmu_time, d.text))
	df = pd.DataFrame()  # 初始化一个DataFrame对象
	df['视频地址'] = video_url_list
	df['弹幕地址'] = danmu_url_list
	df['弹幕时间'] = time_list
	df['弹幕内容'] = text_list
	if os.path.exists(v_result_file):  # 如果文件存在，不需写入字段标题
		header = None
	else:  # 如果文件不存在，说明是第一次新建文件，需写入字段标题
		header = ['视频地址', '弹幕地址', '弹幕时间', '弹幕内容']
	df.to_csv(v_result_file, encoding='utf_8_sig', mode='a+', index=False, header=header)  # 数据保存到csv文件


if __name__ == "__main__":
	print('爬虫程序开始执行！')
	# 保存数据的文件名
	csv_file = '刘畊宏弹幕.csv'
	# 如果存在csv文件，先删除，避免数据重复
	if os.path.exists(csv_file):
		print('{}已存在，开始删除文件'.format(csv_file))
		os.remove(csv_file)
		print('{}已删除文件'.format(csv_file))
	# "刘畊宏"弹幕数较多的视频Bv号
	bv_list = ['BV1Pa411v7vg', 'BV1t3411T7k6', 'BV1wY411P7cV', 'BV1fr4y1J7tL', 'BV1o44y1N7X9']
	# 开始爬取
	for bv in bv_list:
		get_bilibili_danmu(v_url='https://www.bilibili.com/video/{}'.format(bv), v_result_file='刘畊宏弹幕.csv')
	print('爬虫程序执行完毕！')
