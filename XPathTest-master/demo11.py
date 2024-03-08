from lxml import etree
html = etree.parse('./practice_BeautifulSoup.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)