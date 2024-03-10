import pandas as pd
import re

'''
1.删除无用列——drop()
2.
'''
#lis.values[:,1].tolist()方法
lis = [[i for i in range(5)] for i in range(5)]
#print(lis)
lis = pd.DataFrame(lis)   #DataFrame是一个代标签的二维数组，但是如何确定行和列？
lis = lis.values[:,1].tolist()    #保持第一维不变，取第二维的第1个元素
lis = [str(txt) for txt in lis] #是lis中的所有元素转成str格式
print(lis)

inputStr = "hello crifan, nihao crifan"
#正则表达式\w-匹配单词字符
#此处\1前面有’（）‘匹配的（\w+）,因此是对前面的正则式的引用
#若\1前面没有用()括起来的匹配，则 \1 表示匹配八进制数字1
#sub()方法：第一个参数正则表达式，第二个参数为用于替换的字符串或函数，第三个参数为被替换的字符串
#此句中 r 使用正则表达式
replacedStr = re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr)
print ("replacedStr=",replacedStr)