import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
map_ = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
res = 0
ans = []


def dfs(y, x, h):
    global cnt
    visited[y][x] = True

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if (
            0 <= newY < N
            and 0 <= newX < N
            and map_[newY][newX] > h
            and not visited[newY][newX]
        ):
            dfs(newY, newX, h)


for h in range(100):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and map_[i][j] > h:
                cnt += 1
                dfs(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break


print(res)
