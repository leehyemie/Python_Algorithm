from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    # dic = {arr[i]: i for i in range(len(arr))}
    queue = deque([(i, p) for i, p in enumerate(arr)])
    
    count = 0

    # 큐가 비면 탈출
    while queue:
        # 일단 꺼냄
        current = queue.popleft()
        # 더 중요한 문서가 있는지
        higher = False

        for item in queue:
            if item[1] > current[1]:
                higher = True
                break
        
        # 더 중요한 문서가 있다
        if higher:
            # 뒤로 가셈
            queue.append(current)
        else: # 아니다 내가 제일 중요하다
            count += 1 # 출력
            
            if current[0] == m:
                print(count)
                break
