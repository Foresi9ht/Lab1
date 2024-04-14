import re
def ch(t):
    pattern = re.compile(r'a.*b')
    return [m.group(0) for i in t for m in [pattern.match(i)] if m]
t = ["applebow", "banana", "acrobatics"]
res = ch(t)
print(res)
