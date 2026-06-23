t_n = 0
f_n = 0

for _ in range(10):
    n = int(input())

    if n % 3 == 0:
        t_n += 1
    if n % 5 == 0:
        f_n += 1

print(t_n, f_n)