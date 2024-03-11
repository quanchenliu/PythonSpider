"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/11
 @Function  : B站弹幕爬虫
"""

import requests
from bs4 import BeautifulSoup 	  	# 爬虫解析页面
import time
import pandas as pd  				# 存入csv文件
import os


"""爬取B站弹幕: param v_url: 视频地址, param v_result_file: 保存文件名, return:"""
def get_bilibili_danmu(bv, result_file):
	headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
	}

	r1 = requests.get(url='https://api.bilibili.com/x/player/pagelist?bvid=' + bv, headers=headers)
	html1 = r1.json()
	cid = html1['data'][0]['cid']									# 获取视频的 cid
	print(cid)
	danmu_url = 'http://comment.bilibili.com/{}.xml'.format(cid)  	# 弹幕地址, 是 XML 文档

	r2 = requests.get(danmu_url)
	html2 = r2.text.encode('raw_unicode_escape') 					# 编码格式
	soup = BeautifulSoup(html2, 'xml')											# 必须使用 xml 解析器
	danmu_list = soup.find_all('d')

	time_list = []  												# 弹幕时间
	text_list = []  												# 弹幕内容
	for d in danmu_list:
		data_split = d['p'].split(',')  							# 按逗号分隔
		temp_time = time.localtime(int(data_split[4]))  			# 转换时间格式
		danmu_time = time.strftime("%Y-%m-%d %H:%M:%S", temp_time)
		time_list.append(danmu_time)
		text_list.append(d.text)

	df = pd.DataFrame()  											# 初始化一个DataFrame对象
	df['弹幕时间'] = time_list
	df['弹幕内容'] = text_list

	if os.path.exists(result_file):  								# 如果文件存在，不需写入字段标题
		header = None
	else:  															# 如果文件不存在，说明是第一次新建文件，需写入字段标题
		header = ['弹幕时间', '弹幕内容']

	# 数据保存到csv文件
	df.to_csv(result_file, encoding='utf_8_sig', mode='a+', index=False, header=header)

def main():
	csv_file = '新疆棉弹幕.csv'  				# 保存数据的文件名

	if os.path.exists(csv_file):  			# 如果存在csv文件，先删除，避免数据重复
		print('{}已存在，开始删除文件'.format(csv_file))
		os.remove(csv_file)
		print('{}已删除文件'.format(csv_file))

	# 读取"新疆棉"弹幕数较多的视频Bv号
	with open('新疆棉播放量最多的几个视频的BV号.txt', 'r', ) as file:
		bv_list = [bv.strip() for bv in file.readlines()]

	# 开始爬取
	for bv in bv_list:
		get_bilibili_danmu(bv, result_file=csv_file)

if __name__ == "__main__":
	print('爬虫程序开始执行！')
	main()
	print('爬虫程序执行完毕！')
