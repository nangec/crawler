# ajax请求
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20

# request = urllib.request.Request()
#获取下载内容 response = urllib.request.urlopen()
# content = response.read().decode()
import urllib.request
import urllib.parse

def create_request(page):
    url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    # 1  0
    # 2  20
    # 3  40

    data = {
        'start':(page-1)*20,
        'limit':20,
    }
    data = urllib.parse.urlencode(data)
    url = url+data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def getcontent(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = getcontent(request)
        down_load(content,page)

