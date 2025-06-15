n, k, i = map(int, input().split(' '))
cnt = 0

while(k!=i):
    k = (k+1)//2
    i = (i+1)// 2
    cnt += 1

print(cnt)