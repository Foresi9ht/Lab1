import re

def ch(t):
    p = '[A-Z][a-z]+'
    m = re.findall(p, t)
    return m

t = "Ola Amigo QUE por Favor?"
m = ch(t)
print(m)
