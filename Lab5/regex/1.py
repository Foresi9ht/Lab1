import re
def s(a,b):
    return bool(re.search(a,b))
a = "ab"
t = ["a b", "bbaab", "abb", "abbb"]
for b in t:
    if s(a,b):
        print(f"'{b}' yes")
    else:
        print(f"'{b}' no")