import unicodedata
import re
import os
import string
from xml.dom.minidom import parse

def twitterPreProcess(xinjiangCotton_path):
    # xinjiangCotton_path=r'C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\twitter数据\原始数据\张占山-新疆棉花\Xinjiang cotton.txt'
    with open(xinjiangCotton_path,'r',encoding='utf-8') as f:
        data=f.readlines()
    contents=[]
    for text in data:
        txt_list=text.split(' ')[5:]
        clean_txt_list=[]
        for i,word in enumerate(txt_list):
            if not word or word[0]=='@' or word=='//' or re.findall(r'((http|ftp|https)://)',word):
                continue
            word = re.sub(r'(#|amp;|gt;)', '', word)
            clean_txt_list.append(word)

        txt=' '.join(clean_txt_list)
        if txt and txt[-1] !='\n':
            txt+='\n'
        txt = "".join(ch for ch in txt if unicodedata.category(ch)[0] != 'S')  # 去除表情等杂乱字符串
        if txt and txt not in contents:
            contents.append(txt)
    contents.sort(key=lambda x:len(x))


    # doc=docx.Document()
    # for c in contents:
    #     doc.add_paragraph(c[:-1])
    # doc.save('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\\twitter.docx')

    # write_path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\\twitter.txt'
    # with open(write_path,'w',encoding='utf-8') as f:
    #     f.writelines(contents)
    return contents
def EngPun_2_ChnPun(str):#中文符号转英文
    EngPun=u',.!?[]()<>""""\'\'\';:---. .   '
    ChnPun=u'，。！？【】（）《》"“"”‘’’；：—-―.….  ️️'
    table={ord(c):ord(e) for e,c in zip(EngPun,ChnPun)}
    return str.translate(table)

def word_punc(word,splitPunc):#用于分割每个word中的符号与标点符号
    str_list=[]
    word=word.strip()
    if not word:
        return None
    while word and word[0] in splitPunc:
        str_list.append(word[0])
        word=word[1:]
    if word:
        if word[-1] not in string.punctuation:
            str_list.append(word)
        else:
            temp=[]
            while word[-1] in string.punctuation:
                temp.append(word[-1])
                word=word[:-1]
            str_list.append(word)
            str_list+=temp[::-1]
    return str_list

def twitter_process(twitter_path,twitter_1_path,twitter_2_path):
    with open(twitter_path,'r',encoding='utf-8') as f:
        data=f.readlines()

    punc = string.punctuation
    # splitPunc=r',.!?\'"()_-<>'
    textdata=[] #存放处理好的text
    textList=[] #存放处理好的text的列表空格形式
    num=0
    for text in data:
        text=text[:-1].strip()   #去除\n和首尾空格
        print(text)
        text = re.sub(re.compile('(h&m)',re.IGNORECASE), 'HM', text)  # 将HM替换成统一表述
        # xjcottonPattern=re.compile('(xinjiang cotton)|(xinjiangcotton)|(xinjiang\'s cotton)',re.IGNORECASE)

        text=re.sub(re.compile('(xinjiang)|(xin jiang)|(xingjiang)|(xiangjiang)',re.IGNORECASE),'Xinjiang',text)
        text = re.sub(re.compile('(xinjiang cotton)|(xinjiangcotton)|(xinjiang\'s cotton)', re.IGNORECASE),
                      'Xinjiang Cotton', text)  # 统一表述
        text=re.sub(re.compile('(forcedlabor)|(forcedlabour)',re.IGNORECASE),'forced labor',text)
        text = re.sub(re.compile('(nike)', re.IGNORECASE), 'NIKE', text)
        text = re.sub(re.compile('(lining)|(li ning)|(li-ning)', re.IGNORECASE), 'LiNing', text)
        text = re.sub(re.compile('(adidas)', re.IGNORECASE), 'Adidas', text)
        text = re.sub(re.compile('(muji)', re.IGNORECASE), 'MUJI', text)
        text = re.sub(re.compile('(uniqlo)', re.IGNORECASE), 'UNIQLO', text)
        text=re.sub(re.compile('u\.s\.',re.IGNORECASE),'US',text)
        text = re.sub(r'\.\.\.', ', ', text)
        text = EngPun_2_ChnPun(text)  # 将中文符号转换成英文符号
        if not text:
            continue
        # text=text.capitalize()  #首字母大写
        text=text.strip()
        if text[-1] in punc:    #去除多余的符号
            while text[-2] in punc:
                text=text[:-1]
            if text[-1] in ['"','\'',')','(','>','<']:
                text+='.'
        else:
            text+='.'   #末尾添加'.'
        if text[-1]==',':
            text=text[:-1]+'.'

        if text+'\n' in textdata:   #去重
            continue
        textdata.append(text+'\n')

        res=re.split(r'(,|\.|!|\?|\'|"|\\|/|\(|\)|_|-|<|>|\s|&|\[|])',text)

        #去除多余的空格以及保存 ‘s ’ll n't 等单词形式
        i,j=0,0
        while j<len(res):
            if res[j]=='' or res[j]==' ':
                j+=1
                continue
            if j!=0 and res[j]=='\'' and res[j-1].isalnum() and res[j+1].isalnum():
                if res[i-1][-1]=='n' and res[j+1]=='t':
                    res[i-1]=res[i-1][:-1]
                    res[i]='n\'t'
                else:
                    res[i]='\''+res[j+1]
                i+=1
                j+=2
                continue
            res[i]=res[j]
            i+=1
            j+=1
        res=res[:i]
        print(res)
        textList.append(' '.join(res)+' '+str(num)+'\n')
        num+=1

    with open(twitter_1_path,'w',encoding='utf-8') as f:
        f.writelines(textdata)
    with open(twitter_2_path, 'w', encoding='utf-8') as f:
        f.writelines(textList)
    for i in range(len(textList)):
        with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\标注数据\数据集v1_1\\twitter_'+str(i)+'.txt','w',encoding='utf-8') as f:
            f.write(textList[i][:-1])

def twitter_generate_v3():
    read_path_0='C:\\Users\\28653\Desktop\\毕业设计\数据集\新疆棉花数据集\\twitter数据\原始数据\张占山-新疆棉花\Xinjiang cotton.txt'
    contents_0=twitterPreProcess(read_path_0)
    read_path_1='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\原始数据\张占山-新疆棉花\事件发生1个月内\总共(去除重复后).txt'
    contents_1=twitterPreProcess(read_path_1)
    read_path_dir='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\原始数据\张占山-新疆棉花\最近7天'
    for read_path_temp in os.listdir(read_path_dir):
        if read_path_temp not in ['Uyghur.txt','”Xinjiang“.txt']:
            contents_1+=twitterPreProcess(read_path_dir+'\\'+read_path_temp)
    contents_1=list(set(contents_1))

    text_data=[txt for txt in contents_1 if txt not in contents_0]
    text_data.sort(key=lambda x:len(x))
    write_path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\\twitter2.txt'
    with open(write_path,'w',encoding='utf-8') as f:
        f.writelines(text_data)
    print(len(text_data))

def cotton_filter():
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\\twitter2-清洗1.txt','r',encoding='utf-8') as f:
        contents=f.readlines()
    i=201
    for txt in contents[201:]:
        if 'cotton' in txt.lower():
            contents[i]=txt
            i+=1
    contents=contents[:i]
    with open('C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\\twitter2-清洗2.txt','w',encoding='utf-8') as f:
        f.writelines(contents)


def single_Twitter_process(twt,isAsp=0):
    # with open(twtPath,'r',encoding='utf-8') as f:
    #     twt=f.readline()
    twt = re.sub(re.compile('(uniqlo)', re.IGNORECASE), 'UNIQLO', twt)
    twt = re.sub(re.compile('u\.s\.', re.IGNORECASE), 'US', twt)

    twt=re.sub('â\x80\x9d','"',twt)
    twt = re.sub('Â', ' ', twt)
    twt = re.sub('â€™', '\'', twt)
    if not isAsp:
        twt=EngPun_2_ChnPun(twt)
        twt=twt.strip()
        twtList=twt.split(' ')[:-1]
    else:

        twt = EngPun_2_ChnPun(twt)
        twt = twt.strip()
        twtList = twt.split(' ')
    res=[]
    for word in twtList:
        if word=='' or word==' ':
            continue
        if '\'' in word:
            index=word.find('\'')
            if 'n\'t' in word:
                res.append(word[:index-1])
                res.append('n\'t')
            else:
                res.append(word[:index])
                res.append(word[index:])
        elif len(word)>1 and word[-1] in [':','"','\'',';']:
            res.append(word[:-1])
            res.append(word[-1])
        elif len(word) > 1 and '/' in word:
            index=word.find('/')
            res.append(word[:index])
            res.append('/')
            if index<len(word)-1:
                res.append(word[index+1:])
        elif len(word) > 1 and '[' in word:
            index=word.find('[')
            res.append(word[:index])
            res.append('[')
            if index<len(word)-1:
                res.append(word[index+1:])
        elif len(word) > 1 and ']' in word:
            index=word.find(']')
            res.append(word[:index])
            res.append(']')
            if index<len(word)-1:
                res.append(word[index+1:])
        elif len(word) > 1 and '-' in word:
            index=word.find('-')
            res.append(word[:index])
            res.append('-')
            if index<len(word)-1:
                res.append(word[index+1:])
        elif len(word) > 1 and '"' in word:
            index=word.find('"')
            res.append(word[:index])
            res.append('"')
            if index<len(word)-1:
                res.append(word[index+1:])
        else:
            res.append(word)
    return res

def generate_bigram(labeledPath,bigramPath):
    xmlLabeledDoc=labeledPath+'\\'+'outputs'
    xmlNums=len(os.listdir(xmlLabeledDoc))

    sentiments = {'asp-positive': 'POS', 'asp-negative': 'NEG', 'asp-neutral': 'NEU'}
    lowerData=[]
    textData=[]
    bigramData=[]
    for num in range(xmlNums):
        xmlPath=os.path.join(xmlLabeledDoc,'twitter_'+str(num)+'.xml')
        DomTree=parse(xmlPath)
        xmldoc=DomTree.documentElement

        textPath=xmldoc.getElementsByTagName('path')[0].childNodes[0].data
        with open(textPath,'r',encoding='utf-8') as f:
            text=f.readline()
        text=single_Twitter_process(text,isAsp=0)
        print(num,text)

        ##去重
        textLower=' '.join(text).lower()
        if textLower not in lowerData:
            lowerData.append(textLower)
            textData.append(text)
        else:
            continue

        items=xmldoc.getElementsByTagName('outputs')[0].getElementsByTagName('annotation')[0].getElementsByTagName('T')[0].getElementsByTagName('item')
        aspList=[]
        for item in items:
            if not item.getElementsByTagName('type'):
                continue
            aspSentiment=item.getElementsByTagName('name')[0].childNodes[0].data
            asp=item.getElementsByTagName('value')[0].childNodes[0].data
            startIndex=int(item.getElementsByTagName('start')[0].childNodes[0].data)
            aspList.append([startIndex,single_Twitter_process(asp,isAsp=1),aspSentiment])
        aspList.sort(key=lambda x:x[0])

        matchIndex=0
        textLen=len(text)
        aspBigram=[]
        for aspItem in aspList:
            asp=aspItem[1]
            aspSenti=sentiments[aspItem[-1]]
            aspLen = len(asp)
            aspIndex=[]

            while matchIndex<textLen:
                if asp[0]==text[matchIndex]:
                    temp = matchIndex
                    aspTemp=[]
                    i=0
                    while i<aspLen:
                        if asp[i] == text[temp]:
                            aspTemp.append(temp)
                            i+=1
                            temp+=1
                        else:
                            break
                    if i>=aspLen:
                        aspIndex=aspTemp
                        matchIndex=temp
                        break
                    else:
                        aspIndex=[]
                        matchIndex += 1
                else:
                    matchIndex+=1

            assert aspIndex!=[], 'Error path:'+str(asp)+xmlPath

            aspBigram.append([aspIndex,aspSenti])
        print(num,' '.join(text)+'#####'+str(aspBigram))
        bigramData.append(' '.join(text)+'#####'+str(aspBigram)+'\n')

    with open(bigramPath,'w',encoding='utf-8') as f:
        f.writelines(bigramData)


if __name__=='__main__':
    # twitterProcess_1()

    # twitter_path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\数据集v1\\twitter3000_v1.txt'
    # twitter_1_path='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\数据集v1\\twitter3000_v1_清洗1_1.txt'
    # twitter_2_path = 'C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\处理数据\数据集v1\\twitter3000_v1_清洗2_1.txt'
    # twitter_process(twitter_path,twitter_1_path,twitter_2_path)

    # twitter_generate_v3()

    # cotton_filter()

    #生成二元组标注数据
    labeledPath='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\标注数据\数据集v1'
    bigramPath='C:\\Users\\28653\Desktop\毕业设计\数据集\新疆棉花数据集\\twitter数据\标注数据\\results_v1.txt'
    generate_bigram(labeledPath,bigramPath)