import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())


matrix = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = True
    matrix[y][x] = True


def dfs(idx):
    global cnt
    visited[idx] = True

    for i in range(1, N + 1):
        if not visited[i] and matrix[idx][i]:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
