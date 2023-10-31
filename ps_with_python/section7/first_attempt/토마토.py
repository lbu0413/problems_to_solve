import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for i in range(M):
    for j in range(N):
        if map_[i][j] == 1:
            dq.append((i, j))

while dq:
    tmp = dq.popleft()
    for k in range(4):
        newY = tmp[0] + dy[k]
        newX = tmp[1] + dx[k]

        if 0 <= newY < M and 0 <= newX < N and map_[newY][newX] == 0:
            map_[newY][newX] = 1
            visited[newY][newX] = visited[tmp[0]][tmp[1]] + 1
            dq.append((newY, newX))

flag = 1
for i in range(M):
    for j in range(N):
        if map_[i][j] == 0:
            flag = -1

if flag == 1:
    print(max(max(x) for x in visited))
else:
    print(flag)
