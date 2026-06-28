N = int(input())

for i in range(N):
    if i % 2 == 0:  # 짝수 번째 줄
        for j in range(1, N + 1):
            print(j, end="")
    else:  # 홀수 번째 줄
        for j in range(N, 0, -1):
            print(j, end="")
    print()