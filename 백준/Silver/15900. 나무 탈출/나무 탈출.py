import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs():
    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[current] + 1
                queue.append(neighbor)

bfs()

total = 0
for i in range(2, n + 1):
    # 루트가 아닌 리프 노드만 카운트
    if len(graph[i]) == 1 and i != 1:
        total += depth[i]

print("Yes" if total % 2 == 1 else "No")
