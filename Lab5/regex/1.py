import re
def s(a,b):
    return bool(re.search(a,b))
a="ab+"
t = ["a", "ab", "abb", "abbb", "ac", "bc", "b"]
for b in t:
    if s(a,b):
        print(f"'{b}' yes")
    else:
        print(f"'{b}' no")