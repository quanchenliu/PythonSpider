"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/11
 @Function  : B站弹幕情感分析
"""
import pandas as pd  # 数据分析库
from snownlp import SnowNLP  # 中文情感分析库
from wordcloud import WordCloud  # 绘制词云图
from pprint import pprint  # 美观打印
import jieba.analyse  # jieba分词
from PIL import Image  # 读取图片
import numpy as np  # 将图片的像素点转换成矩阵数据
import matplotlib.pyplot as plt  # 画图

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签, 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 情感分析打标
def sentiment_analyse(barrage_list):
    score_list = []  # 情感评分值
    tag_list = []  # 打标分类结果
    opt_count = 0  # 计数器-积极
    neg_count = 0  # 计数器-消极
    mid_count = 0  # 计数器-中性

    for barrage in barrage_list:
        tag = ''
        sentiments_score = SnowNLP(barrage).sentiments
        if sentiments_score < 0.5:
            tag = '消极'
            neg_count += 1
        elif sentiments_score > 0.5:
            tag = '积极'
            opt_count += 1
        else:
            tag = '中性'
            mid_count += 1
        score_list.append(sentiments_score)  # 得分值
        tag_list.append(tag)  # 判定结果
    df['情感得分'] = score_list
    df['分析结果'] = tag_list
    grp = df['分析结果'].value_counts()
    print('正负面评论统计：')
    print(grp)
    grp.plot.pie(y='分析结果', autopct='%.2f%%')  # 画饼图
    plt.title('刘畊宏弹幕_情感分布占比图',fontproperties='SimHei')
    plt.savefig('刘畊宏弹幕_情感分布占比图.png')  # 保存图片
    # 把情感分析结果保存到excel文件
    df.to_excel('刘畊宏弹幕_情感评分结果.xlsx', index=None)
    print('情感分析结果已生成：刘畊宏_情感评分结果.xlsx')


# 绘制词云图
def make_wordcloud(v_str, v_stopwords, v_outfile):
    print('开始生成词云图: {}'.format(v_outfile))
    try:
        stopwords = v_stopwords  # 停用词
        backgroud_Image = np.array(Image.open('刘畊宏_背景图.png'))  # 读取背景图片
        wc = WordCloud(
            background_color="white",  # 背景颜色
            width=1500,  # 图宽
            height=1200,  # 图高
            max_words=1000,  # 最多字数
            # font_path='/System/Library/Fonts/SimHei.ttf',  # 字体文件路径，根据实际情况(Mac)替换
            font_path="C:\Windows\Fonts\simhei.ttf",  # 字体文件路径，根据实际情况(Windows)替换
            stopwords=stopwords,  # 停用词
            mask=backgroud_Image,  # 背景图片
        )
        jieba_text = " ".join(jieba.lcut(v_str))  # jieba分词
        wc.generate_from_text(jieba_text)  # 生成词云图
        wc.to_file(v_outfile)  # 保存图片文件
        print('词云文件保存成功：{}'.format(v_outfile))
    except Exception as e:
        print('make_wordcloud except: {}'.format(str(e)))


def main():
    # 获取评论内容列表:
    # .values 将 DataFrame 列转换为 NumPy 数组
    # .tolist() 方法将该数组转换为 Python 列表
    df = pd.read_csv('新疆棉弹幕.csv')
    barrage_list = df['弹幕内容'].values.tolist()
    print('length of v_cmt_list is:{}'.format(len(barrage_list)))

    barrage_list = [str(i) for i in barrage_list]  # 将所有元素转换成字符串
    barrage_str = ' '.join(str(i) for i in barrage_list)  # 将所有内容连接成一个字符串, 并以空格为分隔符

    # 1、情感分析打分
    sentiment_analyse(barrage_list=barrage_list)

    # 2、用jieba统计弹幕中的top10高频词
    keywords_top10 = jieba.analyse.extract_tags(barrage_str, withWeight=True, topK=10)
    print('top10关键词及权重：')
    pprint(keywords_top10)
    with open('新疆棉TOP10高频词.txt', 'w') as f:
        f.write(str(keywords_top10))

    # 3、画词云图
    make_wordcloud(v_str=barrage_str,
                   # 停用词
                   v_stopwords=['这个', '吗', '的', '啊', '她', '是', '了', '你', '我', '都', '也', '不', '在', '吧',
                                '说', '就是', '这',
                                '有', '就', '或', '哇', '哦', '这样', '真的'],
                   # 词云图文件名
                   v_outfile='新疆棉弹幕_词云图.jpg'
                   )


if __name__ == '__main__':
    print('情感分析程序开始执行！')
    main()
    print('情感分析程序执行完毕！')