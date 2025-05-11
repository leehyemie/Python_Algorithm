from collections import deque

# 8방향 이동 (상하좌우 + 대각선)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# BFS를 위한 큐와 거리 배열
queue = deque()
dist = [[-1]*m for _ in range(n)]

# 아기 상어가 있는 칸은 거리 0, 큐에 먼저 넣기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

# BFS 수행
while queue:
    x, y = queue.popleft()
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

# 안전 거리의 최댓값 찾기
max_distance = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] > max_distance:
            max_distance = dist[i][j]

print(max_distance)
