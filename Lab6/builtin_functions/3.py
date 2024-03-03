def palindrome(s):
    return s == s[::-1]

input_str = input()
if palindrome(input_str):
    print("Palindrome")
else:
    print("Not a palindrome")
