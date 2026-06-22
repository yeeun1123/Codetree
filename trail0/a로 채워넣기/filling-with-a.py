s = input()

s = list(s)

s[1] = 'a'      # 앞에서 2번째 문자
s[-2] = 'a'     # 뒤에서 2번째 문자

print(''.join(s))