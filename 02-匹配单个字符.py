import re
# res=re.match('.','python')
# res=re.match('t.o','t@o')
# res=re.match('t..o','twwo')
# res=re.match('t.o','t\no')


# res=re.match('[h]','hello')
# res=re.match('[hH]','Hello')

# res=re.match('[0123456789]','6djhjhdd')
# res=re.match('[a-zA-Z0-9]','dsjdksjdksj')


# res=re.match('\d','$')
# res=re.match('t\do','t2o')

# res=re.match('\D','$')
# res=re.match('\D','dhkdjhkjh')


# res=re.match('t\sd','t d')
# res=re.match('t\sd','t\td')
# res=re.match('t\s\s\so','t   o')


# res=re.match('t\So','two')
# res=re.match('t\So','t\to')

# res=re.match('t\wo','two')
# res=re.match('t\wo','t_o')
# res=re.match('t\wo','t9o')
# res=re.match('t\wo','tWo')
# res=re.match('t\wo','t二o')


# res=re.match('t\Wo','t@o')
res=re.match('t\Wo','t\no')
if res:
    print(f'匹配的内容为:{res.group()}')
else:
    print('匹配失败...')