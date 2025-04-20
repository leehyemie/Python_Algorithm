from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

   # (중요도, 문서)
    queue = deque([(p, i) for i, p in enumerate(arr)])   
    count = 0

    # 큐가 비면 탈출
    while queue:
        # 일단 꺼냄
        current = queue.popleft() # current = (1, 0)
        # 더 중요한 문서가 있는지
        lower = False

        for item in queue:
            # 더 중요한 문서가 존재
            if item[0] > current[0]:
                lower = True
                break
        
        # 더 중요한 문서가 있다
        if lower:
            # 뒤로 가셈
            queue.append(current)
        else: # 아니다 내가 제일 중요하다
            count += 1 # 출력
            
            # 타겟 문서인지 확인
            if current[1] == m:
                print(count)
                break



    


