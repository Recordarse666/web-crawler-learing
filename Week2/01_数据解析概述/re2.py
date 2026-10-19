import re

# findall：返回所有匹配，直接是列表
lst = re.findall(r"\d+", '我的电话号是：10086')
print(lst)                              # ['10086']

# finditer：返回迭代器，需 .group() 取值
it = re.finditer(r"\d+", '我的电话号是：10086')
for i in it:
    print(i.group())                    # 10086

# search：第一个匹配，需 .group()
res = re.search(r"\d+", '我的电话号是：10086')
print(res.group())                      # 10086

# match：必须从头匹配，需 .group()
res = re.match(r"\d+", '10086')
print(res.group())                      # 10086

# compile：预加载，重复使用
pattern = re.compile(r"\d+")
print(pattern.findall('我的电话号是：10086'))  # ['10086']

s = '''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>王一博</span></div>
'''

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d)'>(?P<wahaha>.*?)</span></div>", re.S)
result = obj.finditer(s)
for i in result:
    print(i.group("id"))
# 命名捕获组：(?P<...>) → 固定开头，P 是 Python 的意思！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1
# wahaha → 你自己起的组名（可换成 name、title、content 等）
# .*? → 要捕获的内容（这里是 div 里的人名）