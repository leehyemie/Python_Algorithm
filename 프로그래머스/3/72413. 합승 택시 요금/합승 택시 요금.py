import heapq
from collections import defaultdict

def dijkstra(start, n, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]  # (비용, 노드)

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distance

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))  # 양방향

    # s, a, b에서 각각 다익스트라
    dist_s = dijkstra(s, n, graph)
    dist_a = dijkstra(a, n, graph)
    dist_b = dijkstra(b, n, graph)

    # 가능한 모든 경유지 k (1부터 n까지)에 대해 최소 비용 계산
    min_cost = float('inf')
    for k in range(1, n + 1):
        total_cost = dist_s[k] + dist_a[k] + dist_b[k]
        min_cost = min(min_cost, total_cost)

    return min_cost
