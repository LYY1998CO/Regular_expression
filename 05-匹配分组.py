import  re
# res=re.match('abc|python','abc')
# res=re.match('abc|python','python')

# res=re.match('([a-zA-Z0-9]{4,10})@(qq|163)\.com$','hello@qq.com')
# my_str='<div>这是一个块标签</div>'
# res=re.match('<([a-zA-Z0-9]+)>.*</\\1>',my_str)
my_str='<html><div>这是一个嵌套标签</div></html>'
# res=re.match('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>',my_str)
res=re.match('<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name1)>',my_str)



if res:
    print(f'匹配的结果为:{res.group()}')
else:
    print('匹配失败...')