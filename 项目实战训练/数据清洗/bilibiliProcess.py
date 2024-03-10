import pandas as pd
import re

'''
1.删除无用列——drop()
2.
'''

#粗处理

def EngPun_2_ChnPun(str):   #英文符号转中文
    #制作翻译表
    EngPun=u',!?[]()<>"\';:'
    ChnPun=u'，！？【】（）《》“‘；：'
    table={ord(e):ord(c) for e,c in zip(EngPun,ChnPun)}  #ord()方法返回字符的ASCII码或Unicode数值,从而构建出翻译表
    return str.translate(table) #返回的是，

def bilibiliprocess_1():
    path='E:\学习资料（主）\大三\舆情控制\\venv\\b站爬虫\\b站评论.xlsx'
    texts=pd.read_excel(io=path)
    texts=texts.values[:,3].tolist()        #保持第一维不变，取第二维的第1个元素
    texts = [str(txt) for txt in texts]     #将texts转换成str类型的数据















    #完成英中文转换
    texts = [EngPun_2_ChnPun(str(txt)) for txt in texts if str(txt) != 'nan']   #对texts中的每一个str类型数据调用EngPun_2_ChnPun函数

    textsData = []
    for text in texts:
        text = text.upper()  # 小写转大写
        # sub()方法：第一个参数正则表达式，第二个参数为用于替换的字符串或函数，第三个参数为被替换的字符串
        # 此句中 r 使用正则表达式
        text = re.sub(r'&', '', text)
        textsData.append(text)  #末尾加入元素

    with open('E:\学习资料（主）\大三\舆情控制\\venv\\b站爬虫\\b站评论.txt','w',encoding='utf-8') as f:
        f.writelines('\n'.join(textsData))

if __name__=='__main__':
    bilibiliprocess_1()

