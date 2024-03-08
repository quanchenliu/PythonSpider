from lxml import etree

html = etree.parse('./practice_BeautifulSoup.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))