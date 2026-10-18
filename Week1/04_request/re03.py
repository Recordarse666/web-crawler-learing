#XHR
import requests
url='https://movie.douban.com/j/chart/top_list'

#重新封装参数
param={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'

}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0'
}
resp=requests.get(url=url,params=param,headers=headers)#会对url进行处理，和网页源码上的一样
#print(resp.request.url)
print(resp.json())#啥都没有，被反爬了,加上User-Agent


# User-Agent（UA）= 你每次进网站时递给门卫的名片。
# 它是什么：HTTP 请求头里的一段文字，告诉服务器「我是谁、用什么浏览器、什么系统」。

# 爬虫为什么必须带它：
#
# requests 默认 UA 是 python-requests/2.xx，等于自报家门「我是爬虫」。
# 服务器一看就拦你（就像百度给你的跳转壳）。
# 手动换成 Chrome 的 UA，等于戴上面具假装正常浏览器，就能蒙混过关。




