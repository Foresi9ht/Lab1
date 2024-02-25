import re
def ch(a,b):
    return bool(re.search(a,b))
a="ab{2}$|ab{3}$"
test=["baaaabbbaaabb", "bobr", "abb","amigo","abbb"]
for i in test:
    if ch(a,i):
        print(f"'{i}' yes")
    else:
        print(f"'{i}'no")