import sys
from collections import deque

dq = deque()
input = sys.stdin.readline


map_ = [list(map(int, input().split())) for _ in range(7)]
map_[0][0] = 1
tracker = [[0] * 7 for _ in range(7)]
dq.append((0, 0))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


while dq:
    current = dq.popleft()

    for i in range(4):
        y = current[0] + dy[i]
        x = current[1] + dx[i]

        if 0 <= y <= 6 and 0 <= x <= 6 and map_[y][x] == 0:
            map_[y][x] = 1
            tracker[y][x] = tracker[current[0]][current[1]] + 1
            dq.append((y, x))

print(-1 if tracker[6][6] == 0 else tracker[6][6])
