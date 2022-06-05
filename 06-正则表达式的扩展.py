import re
# res=re.match('hello','Hello',re.I)
# res=re.match('.','\n',re.S)

# res=re.search('abc','111abc222abc')

# res=re.findall('abc','111abc222abc')
# print(res)

# res=re.findall('111(.*)222','111abc222abc')
# print(res)

# res=re.sub('-','*','hello-python-world')
# print(res)

# res=re.sub('-','*','hello-python-world',1)
# print(res)

# res=re.split('-','hello-python-world')
# print(res)

res=re.split('-','hello-python-world',1)
print(res)
# if res:
#     print(f'匹配的内容为:{res.group()}')
# else:
#     print('匹配失败...')