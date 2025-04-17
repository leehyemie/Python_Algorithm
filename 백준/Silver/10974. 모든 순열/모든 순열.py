from itertools import permutations

n = int(input())
s = []

for i in range(1, n+1):
    s.append(i)

for i in permutations(s):
    #print(i)
    #print(list(map(str, i)))
    print(' '.join(map(str, i)))