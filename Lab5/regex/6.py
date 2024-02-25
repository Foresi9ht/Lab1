import re

def rep(t):
    p = '[ ,.]'
    res = re.sub(p, ':', t)
    return res

text = "ola amigo , QUE, por.FAVOR "
res = rep(text)
print(res)