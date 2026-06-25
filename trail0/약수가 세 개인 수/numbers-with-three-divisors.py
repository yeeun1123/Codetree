start, end = map(int, input().split())

count = 0

for n in range(start, end + 1):
    divisor_cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisor_cnt += 1

    if divisor_cnt == 3:
        count += 1

print(count)