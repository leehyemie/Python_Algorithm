n, m = map(int, input().split(' '))
rec = [list(map(int, input())) for _ in range(n)]
size = 1

for i in range(n):
    for j in range(m):
        for x in range(1, min(n-i, m-j)):
            # print("1번째 출력: i = %d, j = %d, x = %d" % (i, j, x))
            if i+x <=n and j+x <= m:
                # print("2번째 출력: i = %d, j = %d, x = %d" % (i, j, x))
                if (rec[i][j] == rec[i+x][j] == rec[i][j+x]==rec[i+x][j+x]):
                    # print("3번째 출력: i = %d, j = %d, x = %d, i+x = %d, j+x = %d" % (i, j, x,i+x,j+x))
                    pre_size = (x+1)*(x+1)
                    size = max(size, pre_size)
print(size)