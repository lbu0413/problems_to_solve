import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[False] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = True

cnt = 0


def dfs(level):
    global cnt
    visited[level] = True

    if level == N:
        cnt += 1

    else:
        for i in range(1, N + 1):
            if not visited[i] and matrix[level][i]:
                dfs(i)
                visited[i] = False


dfs(1)
print(cnt)
