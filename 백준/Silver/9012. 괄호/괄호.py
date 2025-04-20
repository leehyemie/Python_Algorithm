

t = int(input())
arr = []

for _ in range(t):    
    arr.append(input())


for i in range(len(arr)):
    flag = True
    stack = []
    for p in arr[i]:
        # p = arr[i][j]      

        if p == '(':            
            stack.append(p)
            
        else:            
            if not stack:
                print("NO")
                flag = False
                break
            stack.pop()
            
    if flag:
        if not stack:
            print("YES")
        else:
            print("NO")
    


