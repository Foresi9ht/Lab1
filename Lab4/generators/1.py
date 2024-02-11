def num(N):
    for i in range(1, N + 1):
        print(i ** 2)
N = int(input("N:"))
squaregen = num(N)
for square in squaregen:
    print(square)