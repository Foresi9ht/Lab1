import re

def ch(t):
    p='_(.)'
    rep= lambda m: m.group(1).upper()
    res = re.sub(p, rep, t)
    return res

text="sosos_sos_ssos_s"
res=ch(text)
print(res)