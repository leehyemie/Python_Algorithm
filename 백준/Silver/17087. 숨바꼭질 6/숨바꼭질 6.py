import math
from functools import reduce

n, s = map(int, input().split())
a = list(map(int, input().split()))
d = []

for x in a:
    d.append(abs(x-s))
result = reduce(math.gcd, d)
print(result)