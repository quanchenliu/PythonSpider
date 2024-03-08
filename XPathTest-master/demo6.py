from lxml import etree

html = etree.parse('./practice_BeautifulSoup.html', etree.HTMLParser())
result = html.xpath('//ul/a')
print(result)