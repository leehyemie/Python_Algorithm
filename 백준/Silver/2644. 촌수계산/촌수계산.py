from collections import deque

def find_relation(n, start, end, relations):
    # 1. 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for x, y in relations:
        graph[x].append(y)
        graph[y].append(x)  # 양방향 연결

    # 2. BFS를 통해 최단 거리(촌수) 찾기
    visited = [False] * (n + 1)
    queue = deque()
    queue.append((start, 0))  # (현재 사람, 촌수)
    visited[start] = True

    while queue:
        current, depth = queue.popleft()
        if current == end:
            return depth  # 목적지 도달 시 촌수 반환
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))

    return -1  # 연결되지 않은 경우

# 예제 입력 처리
n = int(input())
start, end = map(int, input().split())
m = int(input())
relations = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(find_relation(n, start, end, relations))
