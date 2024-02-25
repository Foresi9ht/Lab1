import re

def ch(t):
    pattern = re.compile(r'a[a-z]*b$')
    return [m.group(0) for i in t for m in [pattern.match(i)] if m]

t = ["ab", 'aucnrb', ',cjrnfn', 'aknfvhbd','ahgjesfdmbncj']
res = ch(t)
print(res)
