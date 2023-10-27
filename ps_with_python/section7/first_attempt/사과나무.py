import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dq = deque()

sum_ = 0
level = 0

dq.append((N // 2, N // 2))
sum_ += field[N // 2][N // 2]
visited[N // 2][N // 2] = True


while dq:
    if level == N // 2:
        break

    else:
        size = len(dq)
        for i in range(size):
            tmp = dq.popleft()
            for j in range(4):
                y = tmp[0] + dy[j]
                x = tmp[1] + dx[j]
                if not visited[y][x]:
                    visited[y][x] = True
                    sum_ += field[y][x]
                    dq.append((y, x))
        level += 1

print(sum_)
