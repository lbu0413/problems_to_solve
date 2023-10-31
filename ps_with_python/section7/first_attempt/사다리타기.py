import sys

input = sys.stdin.readline

map_ = [list(map(int, input().split())) for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]

dx = [-1, 1]


def dfs(y, x):
    visited[y][x] = True

    if y == 0:
        print(x)
        sys.exit(0)

    for i in range(2):
        newX = x + dx[i]
        if 0 <= newX < 10 and not visited[y][newX] and map_[y][newX] == 1:
            dfs(y, newX)

    dfs(y - 1, x)


for j in range(10):
    if map_[9][j] == 2:
        dfs(9, j)
