n = int(input())
li = []
for _ in range(n):
    key, val = map(str, input().split(' '))
    li.append((int(key), val))

# key, val = map(str, input().split(' '))
# dic = {key: val}

# print(list)
# list.sort()
# print(list)
li.sort(key=lambda x:(x[0]))

for x in li:
    print(x[0], x[1])
