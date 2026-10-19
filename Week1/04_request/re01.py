import requests
wd=input('请输入搜索内容：')
url=f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={wd}'

hea={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

resp=requests.get(url,headers=hea)#处理一个小反爬
print(resp)
print(resp.text)#页面源代码

resp.close()
