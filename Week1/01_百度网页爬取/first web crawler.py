#需求：用程序模拟浏览器，输入一个网址，从网址中获取资源或内容
from urllib.request import urlopen

url="http://www.baidu.com"
resp=urlopen(url)


#print(resp.read().decode('utf-8'))#读取内容,decode解码，从网页中查看编码格式

with open("mybaidu.html",mode='w',encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))#读取到网页的页面源代码
print('over')
