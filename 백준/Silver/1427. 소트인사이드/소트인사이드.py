n = str(input())
arr = []

for x in n:
    arr.append(int(x))
   
arr.sort(reverse = True)

for x in arr:
    print(x, end='')
