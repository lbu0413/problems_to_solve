import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 10000
visited = [False] * MAX
tracker = [0] * MAX

dq = deque()
dq.append(N)
visited[N] = True

while dq:
    current = dq.popleft()

    if next == M:
        print(tracker[next])
        break

    for next in (current + 1, current - 1, current + 5):
        if not visited[next] and 0 < next <= MAX:
            visited[next] = True
            dq.append(next)
            tracker[next] = tracker[current] + 1
