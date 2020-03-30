# import urllib.request
#
# url = 'https://www.jd.com'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# }
#
# request = urllib.request.Request(url=url, headers=headers)
#
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')
#
# with open('jd.html','w',encoding='utf-8') as fp:
#     fp.write(content)

# 京东js加密
from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.jd.com'
browser.get(url)
content = browser.page_source
with open('jd.html','w',encoding='utf-8') as fp:
    fp.write(content)
