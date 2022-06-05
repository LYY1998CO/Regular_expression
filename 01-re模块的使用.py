import re
str1='itcast.cn'
res=re.match('itcast',str1)
# print(res)
if res:
    print(res.group())
else:
    print('匹配失败了...')