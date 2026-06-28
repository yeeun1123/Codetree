N = int(input())

for i in range(N):
    a = i + 1
    b = N - i
    
    for j in range(N):
        if j % 2 == 0:
            print(a, end="")
        else:
            print(b, end="")
    
    print()