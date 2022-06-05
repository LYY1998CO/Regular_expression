# 1.匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# 2.匹配出11位手机号码 第二位是：35789
# 3.匹配出微博中的话题, 比如: #幸福是奋斗出来的#

import re
res=re.match('[a-zA-Z0-9_]{4,20}@163\.com$','hello@163.com')
print(res.group())

res1=re.match('1[35789]\d{9}$','17673640741')
print(res1.group())

res2=re.match('#\w{4,20}(#?)$','#幸福是奋斗出来的#')
print(res2.group())
