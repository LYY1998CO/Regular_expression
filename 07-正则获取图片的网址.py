# <img src="https://img.lianzhixiu.com/uploads/allimg/202004/9999/rne21c4feb74.jpg"
# alt="蕾丝美女嫩玉体若隐若现细腰长腿控宅男福利写真" border="0" />

import re

with open('./meinv.html','r',encoding='gbk') as f:
    data=f.read()

res=re.findall('<img src="(.*?)"',data)
print(res)
for i in res:
    print(i)