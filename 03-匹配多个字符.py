import re
# res=re.match('[a-z]*','ses')
# res=re.match('t.*o','t你尽快老师讲的o')

# res=re.match('t.+o','to')
# res=re.match('[a-zA-Z0-9]+','989')

# res=re.match('t\d?o','t9o')
# res=re.match('t\d?o','to')

# res=re.match('1\d{10}','11234563894')
# res=re.match('1\d{10}','1123456389479789743857384738')

# res=re.match('[a-zA-Z0-9]{4,10}','qwer')
res=re.match('[a-zA-Z0-9]{4,10}','@#qwer')


if res:
    print(f'匹配得内容为:{res.group()}')
else:
    print('匹配失败...')