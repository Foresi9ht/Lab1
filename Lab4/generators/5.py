def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Number: "))
for num in countdown(n):
    print(num)