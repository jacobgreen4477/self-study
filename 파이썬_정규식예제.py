# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:29:58 2018

@author: jacob
"""

import re

lines = [
'fsdafas 00- dfd [dfsd] "GET /vid/eo/a.gif 200 32',        
'fsdafas 00- dfd [dfsd] "GET /vid/eo/b.gif 200 32',
'fsdafas 00- dfd [dfsd] "GET /vid/eo/c.GIF 200 32',
'fsdafas 00- dfd [dfsd] "POST /vi/deo/d.gif 200 32',
'fsdafas 00- dfd [dfsd] "GET /vid/eo/e.gif 100 32'
]


# extract string between two patterns
# GET과 200사이의 문자 가져오기 
out = []
for line in lines:
    try:
        out.append(re.search('GET(.*)200',line).group())
    except:
        pass 

print(out)
lines2 = out


# extract [*.gif] file names 
# 제거할 문자 : [^.]
# 가져올 문자 : .gif
out2 = []
for line in lines2:
    try:
        out2.append(re.search('[^.].gif',line).group())
    except:
        pass 

print(out2)


# 위에 두개를 하나로 만들어 보자 
out = []
for line in lines:
    try:
        tmp = re.search('GET(.*)200',line).group()
        tmp = re.search('[^.].gif',tmp).group()
        out.append(tmp)
    except:
        pass 

print(out)





