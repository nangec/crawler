import urllib.request
from lxml import etree

url = 'http://quote.stockstar.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
request = urllib.request.Request(url=url,headers=headers)
reponse = urllib.request.urlopen(request)
content = reponse.read().decode('gb2312')

tree = etree.HTML(content)
name_list = tree.xpath('//tbody[@class="tbody_right"]//a/text()')
price_list = tree.xpath('//tbody[@class="tbody_right"]//td[7]/text()')
# print(name_list)
# print(price_list)
for i in range(len(name_list)):
    name = name_list[i]
    price = price_list[i]
    print(name,price)