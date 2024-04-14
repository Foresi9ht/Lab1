import re
def find_sequences(text):
    pattern ='[a-z_]+[a-z]'
    matches = re.findall(pattern, text)
    return matches
text = "do_not be_so_Stupid"
matches = find_sequences(text)
print(matches)