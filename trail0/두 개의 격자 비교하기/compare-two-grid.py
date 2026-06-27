# N(행)과 M(열) 크기 입력받기
n, m = map(int, input().split())

# 첫 번째 격자 입력받기
grid1 = [list(map(int, input().split())) for _ in range(n)]

# 두 번째 격자 입력받기
grid2 = [list(map(int, input().split())) for _ in range(n)]

# 두 격자를 비교하며 새로운 격자 출력하기
for i in range(n):
    for j in range(m):
        # 같은 위치의 값이 같으면 0, 다르면 1
        if grid1[i][j] == grid2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()  # 한 행이 끝날 때마다 줄바꿈