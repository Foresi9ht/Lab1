def divnum(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            print(num)
n = int(input("n:"))
divnum(n)