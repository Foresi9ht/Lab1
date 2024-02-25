import re

def ch(t):
    p = '([A-Z])'
    c=lambda m: "_"+m.group(0).lower()
    z = re.sub(p,c, t)
    return z

t = "olaAmigoQuePorFavor?"
res = ch(t)
print(res)