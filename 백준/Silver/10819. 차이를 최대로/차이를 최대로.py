import itertools

n = int(input())
arr = list(map(int, input().split(' ')))
npr = list(itertools.permutations(arr, n))
sum = 0

for i in range(len(npr)):
    pre_sum = 0
    # print(npr[i])
    for j in range(n-1):        
        # print("i = %d, j = %d, npr[i][j] = %d, npr[i][j+1] = %d" %(i, j,npr[i][j], npr[i][j+1]))
        pre_sum += abs(int(npr[i][j]) - int(npr[i][j+1]))
        sum = max(sum, pre_sum)
        
    # print("sum = %d" %(sum))
    # print()

print(sum)

   