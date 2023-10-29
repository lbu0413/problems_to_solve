import sys

input = sys.stdin.readline

map_ = [list(map(int, input().split())) for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0


def dfs(y, x):
    global cnt
    visited[y][x] = True

    if y == 6 and x == 6:
        cnt += 1
        return

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if (
            0 <= newY <= 6
            and 0 <= newX <= 6
            and not visited[newY][newX]
            and map_[newY][newX] == 0
        ):
            dfs(newY, newX)
            visited[newY][newX] = False


dfs(0, 0)
print(cnt)


# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 0
