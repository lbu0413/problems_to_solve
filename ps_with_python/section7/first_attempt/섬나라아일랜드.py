import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

map_ = [list(map(int, input().split())) for _ in range(N)]

# visited 배열 없이 BFS로 풀기

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

cnt = 0

dq = deque()

for i in range(N):
    for j in range(N):
        if map_[i][j] == 1:
            map_[i][j] = 0
            dq.append((i, j))
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    newY = tmp[0] + dy[k]
                    newX = tmp[1] + dx[k]

                    if 0 <= newY < N and 0 <= newX < N and map_[newY][newX] == 1:
                        map_[newY][newX] = 0
                        dq.append((newY, newX))
            cnt += 1

print(cnt)
