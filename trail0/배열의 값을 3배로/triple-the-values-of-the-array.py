arr = []

for i in range(3):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(3):
    for j in range(3):
        print(arr[i][j] * 3, end=" ")
    print()