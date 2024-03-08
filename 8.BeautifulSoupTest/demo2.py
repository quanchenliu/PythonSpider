"""
 -*- coding : utf-8 -*-
 @Author  	: quanchenliu
 @Time	   	: 2024/3/8
 @Function  : BeautifulSoup 的基本用法（关联选择——获取子孙节点、祖先节点）
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('practice_BeautifulSoup.html'), 'lxml')
print(soup.p.contents)          # content 属性: 返回的是由直接子节点组成的列表
print('\n', '//////////////////////////////////////////////////////////////')


print(soup.p.children)          # children 属性: 返回的是一个包含直接子节点的生成器
for i, child in enumerate(soup.p.children):
    print(i, child)             # 通过循环输出相应内容，只迭代生成 直接子节点
print('\n', '//////////////////////////////////////////////////////////////')


print(soup.p.descendants)       # desecndants 属性: 返回的是一个包含所有子孙节点的生成器
for i, child in enumerate(soup.p.descendants):
    print(i, child)             # descendants 会将所有 子节点、孙子节点、子孙节点 都单独迭代生成
print('\n', '//////////////////////////////////////////////////////////////')


print(soup.p.parent)            # parent 属性: 获取节点元素的直接父节点，返回的是父节点的全部内容
print(soup.p.parents)           # parents 属性: 获取所有祖先节点，返回的是一个生成器
print(list(enumerate(soup.p.parents)))
print('\n', '//////////////////////////////////////////////////////////////')


print('Next Sibling', soup.a.next_sibling)                          # Next Sibling: 下一个兄弟节点
print('Prev Sibling', soup.a.previous_sibling)                      # Prev Sibling: 上一个兄弟节点
print('Next Siblings', list(enumerate(soup.a.next_siblings)))       # Next Siblings: 后面所有兄弟节点
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))   # Prev Siblings: 前面所有兄弟节点