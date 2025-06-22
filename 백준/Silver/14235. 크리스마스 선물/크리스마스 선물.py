import heapq
import sys

# 입력 수
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    inputs = list(map(int, sys.stdin.readline().split()))
    a = inputs[0]
    values = inputs[1:]

    if a == 0:
        if heap:
            print(-heapq.heappop(heap))  # 가장 가치 높은 선물
        else:
            print(-1)
    else:
        for v in values:
            heapq.heappush(heap, -v)  # 음수로 push하여 max heap처럼 사용
