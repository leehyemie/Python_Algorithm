import sys
from collections import deque

n = int(sys.stdin.readline())
# 인접리스트로 트리 표현 (1~n)-> 노드 번호가 1번부터 시작해서
graph = [[] for _ in range(n+1)]

# 여기서부터
# n-1개의 간선을 입력 받아 양방향 연결
for _ in range(n-1):
    a, b = map(int, input().split())
    # a, b 서로 연결
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# 부모 정보를 저장할 리스트 (인덱스가 노드 번호)
parent = [0] * (n+1)

queue = deque()
queue.append(1) # 루트 노드 1

while queue:
    # 현재 노드 꺼내기
    current = queue.popleft()
    
    # 현재 노드에 연결된 이웃 노드를 확인
    for neighbor in graph[current]:
        # 아직 부모가 정해지지 않은 노드라면(아직 방문 안 함)
        if parent[neighbor] == 0:
            # 현재 노드를 이웃의 부모로 저장
            parent[neighbor] = current
            # 이웃 노드를 큐에 넣어 계속 탐색
            queue.append(neighbor)

# print("parent[3] =", parent[3])
for i in range(2, n+1):
    print(parent[i])