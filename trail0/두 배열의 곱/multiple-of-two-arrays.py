# 첫 번째 3행 3열 배열 입력받기
array1 = [list(map(int, input().split())) for _ in range(3)]

# 빈 줄 처리 (입력 예제에서 두 배열 사이에 공백이 있을 경우를 대비)
# 만약 입력이 연속으로 들어온다면 이 부분은 생략해도 됩니다.
try:
    input() 
except EOFError:
    pass

# 두 번째 3행 3열 배열 입력받기
array2 = [list(map(int, input().split())) for _ in range(3)]

# 결과 계산 및 출력
for i in range(3):
    for j in range(3):
        # 같은 위치(i행 j열)의 요소를 곱함
        result = array1[i][j] * array2[i][j]
        print(result, end=" ")
    print()  # 한 행이 끝나면 줄바꿈