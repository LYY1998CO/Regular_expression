import re
# res=re.match('[a-zA-Z0-9]{4,10}','qwer1321321313')

# res=re.match('[a-zA-Z0-9]{4,10}$','qwer111111234')

# res=re.match('^[a-z].*','tw')
# res=re.match('[a-zA-Z].*','123abc')

# res=re.match('[a-zA-Z].*[a-zA-Z]','a13_D')

res=re.match('[^0-9]','0')
# res=re.match('[0-9]','0')
if res:
    print(f'匹配的内容为:{res.group()}')
else:
    print('匹配失败....')