import re

def ch(s):
    parts = re.findall('[A-Z][^A-Z]*', s)
    return parts


string = "WouldYouLikeSomeTea?"
result = ch(string)
print(result)