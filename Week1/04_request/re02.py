#使用request获取百度翻译的结果
import requests
url='https://fanyi.baidu.com/sug'

s=input('请输入翻译内容：')
data1={
    'kw':s
}

#发送post请求,发送的数据必须放在字典中，通过data参数进行传递！！！！！！！！！！！！！！！！！！！
resp=requests.post(url,data=data1)
print(resp.json())#将服务器返回的内容直接处理成json()
resp.close()