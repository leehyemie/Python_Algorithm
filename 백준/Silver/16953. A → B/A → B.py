A, B = map(int, input().split())
cnt = 1  # 연산 횟수 (초기값 1)

while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break
    cnt += 1

print(cnt if B == A else -1)
