import sys

input = sys.stdin.readline

N = int(input())

map_ = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = []


def dfs(y, x):
    global cnt
    visited[y][x] = True
    cnt += 1
    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if (
            0 <= newY < N
            and 0 <= newX < N
            and not visited[newY][newX]
            and map_[newY][newX] == 1
        ):
            dfs(newY, newX)


for i in range(N):
    for j in range(N):
        if map_[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for x in ans:
    print(x)
