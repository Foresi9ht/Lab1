def upper_lower(string):
    upperc = sum(1 for char in string if char.isupper())
    lowerc = sum(1 for char in string if char.islower())
    return upperc, lowerc

input_string = input()
upper, lower = upper_lower(input_string)
print("Upper num:", upper)
print("Lower num:", lower)
