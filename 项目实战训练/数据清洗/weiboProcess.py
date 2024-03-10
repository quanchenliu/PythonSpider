import csv
import re
import unicodedata
import string
def weiboProcess_1():#粗处理
    weiboTexts=[]
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\原始数据\数据三\新疆棉花集中营.csv','r',encoding='utf-8') as f:
        reader_1=csv.reader(f)
        weiboTexts += [row[4] for row in reader_1]
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\原始数据\数据三\新疆棉花强迫劳动.csv','r',encoding='utf-8') as f:
        reader_2=csv.reader(f)
        weiboTexts += [row[4] for row in reader_2]

    newweiboTexts=[]

    pattern1=r'(太平鸟)|(【￥)|(景甜跳)'
    pattern2=r''
    for text in weiboTexts:
        if re.findall(pattern1,text) :
            continue
        text = "".join(ch for ch in text if unicodedata.category(ch)[0] != 'S')     #去除表情等杂乱字符串
        text=re.sub(r'[O网页链接]|[&]|[@]','',text)
        text = re.sub(r'L(.)*的微博视频','',text)
        # text = re.sub(r'[#]', '，', text)
        # if text[0]=='，':
        #     text=text[1:]
        if text[-1]=='O':
            text=text[:-1]
        # if text not in newweiboTexts and '疆棉' in text:
        if text not in newweiboTexts:
            newweiboTexts.append(text.upper())
    newweiboTexts=list(set(newweiboTexts))
    newweiboTexts.sort(key=lambda x:len(x))
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\清洗数据\weibo_3_camps.txt','w',encoding='utf-8') as f:
        # f.writelines('\n'.join(newweiboTexts[:int(len(newweiboTexts)*0.8)]))
        f.writelines('\n'.join(newweiboTexts))
def EngPun_2_ChnPun(str):#英文符号转中文
    EngPun=u',.!?[]()<>"\';:'
    ChnPun=u'，。！？【】（）《》“‘；：'
    table={ord(e):ord(c) for e,c in zip(EngPun,ChnPun)}
    return str.translate(table)

def correct_text(text):
    text=text.upper()
    text=re.sub(r'(新疆棉中国心)','',text)
    text=re.sub(r'(NIKE禁用新疆棉)','NIKE',text)
    text=re.sub(r'(#BCI下架抵制新疆棉声明是啥操作#)','BCI',text)
    text=re.sub(r'H&M','HM',text)
    while text[0] in list('，。！？：： '):
        text=text[1:]
    return text

def weiboProcess_2():
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\清洗数据\weibo_2_600.txt','r',encoding='utf-8') as f:
        data=f.readlines()
        print(data)
    data_pun=[EngPun_2_ChnPun(txt[:-1]) for txt in data]    #中文符号转英文
    print(data_pun)
    punc=u'。！？'
    textsData=[]
    for i,txt in enumerate(data_pun):   #补充或者修改符号
        if not txt or len(txt)==0:
            continue
        if txt[-1] in ['，','；','：']:
            txt=txt[:-1]
        if txt[-1] not in punc:
            txt+='。'
        if 'LADYGAGA' not in txt:
            textsData.append(correct_text(txt))
    # data_pun.sort(key=lambda x:len(x))
    print(textsData)
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\清洗数据\weibo_2_600_v1.txt','w',encoding='utf-8') as f:
        f.writelines('\n'.join(textsData))
    # for i in range(len(data_pun)):
    #     with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\微博数据\标注数据\weibo_'+str(i)+'.txt','w',encoding='utf-8') as f:
    #         f.write(data_pun[i])
if __name__=='__main__':
    weiboProcess_2()