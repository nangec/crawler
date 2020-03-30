import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.org/user/login.aspx?from='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
content = response.text

def VIEWSTATE():
    tree = etree.HTML(content)
    VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
    print(VIEWSTATE)
    return VIEWSTATE

def VIEWSTATEGENERATOR():
    tree = etree.HTML(content)
    VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    print(VIEWSTATEGENERATOR)
    return VIEWSTATEGENERATOR

def code(session):
    url = 'https://so.gushiwen.org/RandCode.ashx'
    # imgcode = soup.select('#imgCode')[0].attrs.get(src)
    img = session.get(url=url)
    img.encoding = 'utf-8'
    with open('./code/img.jpg', 'wb') as fp:
        fp.write(img.content)
    code = input('请输入验证码：')
    return code

session = requests.session()

data = {
    '__VIEWSTATE': str(VIEWSTATE()),
    '__VIEWSTATEGENERATOR': str(VIEWSTATEGENERATOR()),
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code':code(session),
    'denglu': '登录',
    'from': 'http://so.gushiwen.org/user/collect.aspx'
}


response_index = session.post(url=url, headers=headers,data=data)

url_index = 'https://so.gushiwen.org/user/collect.aspx'
response_index.encoding = 'utf-8'
# response_index = session.get(url=url_index, headers=headers)
content_index = response_index.text

with open('./code/gsc.html','w',encoding='utf-8') as fp:
    fp.write(content_index)
