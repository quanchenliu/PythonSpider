import pandas as pd
import re


def baiduProcess_1():
    path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\百度数据\原始数据\正文.xlsx'
    texts=pd.read_excel(io=path)    #读入excel表格数据
    texts=texts.values[:,0].tolist()    #
    texts=[str(txt) for txt in texts]   #

    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\百度数据\处理数据\\baidu.txt','w',encoding='utf-8') as f:
        f.writelines('\n'.join(texts))

def EngPun_2_ChnPun(str):   #英文符号转中文
    EngPun=u',!?[]()<>"\';:'
    ChnPun=u'，！？【】（）《》“‘；：'
    table={ord(e):ord(c) for e,c in zip(EngPun,ChnPun)}
    return str.translate(table)
def cut_sent(para):
    para = re.sub('([。！？\?])([^”])',r"\1\n\2",para) # 单字符断句符
    para = re.sub('(\.{6})([^”])',r"\1\n\2",para) # 英文省略号
    para = re.sub('(\…{2})([^”])',r"\1\n\2",para) # 中文省略号
    para = re.sub('(”)','”\n',para)   # 把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()       # 段尾如果有多余的\n就去掉它
    #很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

def baiduProcess_2():
    path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\百度数据\原始数据\新疆棉.xlsx'
    texts=pd.read_excel(io=path)    #读入表格数据
    texts=texts.values[:,1].tolist()
    texts=[EngPun_2_ChnPun(str(txt)) for txt in texts if str(txt)!='nan']

    textsData=[]
    for text in texts:
        text=text.upper()   #小写转大写
        text = re.sub(r'&', '', text)

        textsData.append(text)

    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\百度数据\处理数据\\baidu_1.txt','w',encoding='utf-8') as f:
        f.writelines('\n'.join(textsData))

if __name__=='__main__':
    baiduProcess_2()