def evennum(N):
    for i in range(N + 1):
        if i % 2 == 0:
            print(i)
N = int(input("N:"))
evennum(N)