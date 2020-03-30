import urllib.request
from lxml import etree
import json
import jsonpath

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1575101805803&countryId=&cityId=3&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
# with open('tx.json','w',encoding='utf-8')as fp:
#     fp.write(content)

obj = json.load(open('tx.json','r',encoding='utf-8'))
RecruitPostName_list = jsonpath.jsonpath(obj,'$..RecruitPostName')
LocationName_list = jsonpath.jsonpath(obj,'$..LocationName')
# print(RecruitPostName_list)
for i in range(len(LocationName_list)):
    Resc= RecruitPostName_list[i]
    Loc = LocationName_list[i]
    print(Resc,Loc)
