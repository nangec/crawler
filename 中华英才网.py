import urllib.request
from lxml import etree

url = 'http://www.chinahr.com/sou/?keyword=python'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
request = urllib.request.Request(url=url,headers=headers)
reponse = urllib.request.urlopen(request)
content = reponse.read().decode('utf-8')
# print(content)

tree = etree.HTML(content)
comp_list = tree.xpath('//span[@class="e3 cutWord"]/a/text()')
job_list = tree.xpath('//span[@class="e1"]/a/text()')
price_list = tree.xpath('//li[@class="l2"]/span[@class="e2"]/text()')
# print(price_list)
# print(job_list)
for i in range(len(job_list)):
    comp = comp_list[i]
    job = job_list[i]
    price = price_list[i]
    print(comp,job,price)
