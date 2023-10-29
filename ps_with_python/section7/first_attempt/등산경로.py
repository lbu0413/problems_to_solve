import sys

input = sys.stdin.readline

N = int(input())

map_ = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

start = min([min(r) for r in map_])
end = max([max(r) for r in map_])

for i in range(N):
    for j in range(N):
        if map_[i][j] == start:
            start_idx = (i, j)
        if map_[i][j] == end:
            end_idx = (i, j)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cnt = 0


def dfs(y, x):
    global cnt

    visited[y][x] = True

    if map_[y][x] == end:
        cnt += 1
        return

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]

        if 0 <= newY < N and 0 <= newX < N and not visited[newY][newX]:
            if map_[newY][newX] > map_[y][x]:
                dfs(newY, newX)
                visited[newY][newX] = False


dfs(start_idx[0], start_idx[1])
print(cnt)
