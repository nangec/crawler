import urllib.request
import urllib.parse
import re


def create_request(page):
    if page <= 1:
        url = 'http://sc.chinaz.com/tag_tupian/yazhou.html'
    else:
        url = 'http://sc.chinaz.com/tag_tupian/yazhou_%d.html' % page

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    request = urllib.request.Request(url=url)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    return content

from lxml import etree

# 使用正则
# def down_load(content,i):
#     # pattern = re.compile('src2="(.*?)"',re.S)
#     pattern = re.compile('<div class="box picblock col3".*?<img src2="(.*?)" alt="(.*?)">',re.S)
#     src_list = pattern.findall(content)
#     for src in src_list:
#         url=src[0]
#         filename = './meinv/'+src[1]+'.jpg'
#         urllib.request.urlretrieve(url=url,filename=filename)

def down_load(content):
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@id="container"]//img/@src2')
    alt_list = tree.xpath('//div[@id="container"]//img/@alt')

    for i in range(len(src_list)):
        src = src_list[i]
        alt = alt_list[i]
        suffix = src.split('.')[-1]
        filename = './meinv/' + alt +'.' +suffix
        urllib.request.urlretrieve(url=src,filename=filename)

if __name__ == '__main__':
    start_page = int(input('请输入要爬取的起始页数'))
    end_page = int(input('请输入要爬取的结束页数'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)