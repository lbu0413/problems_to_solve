import sys

input = sys.stdin.readline

N, M = map(int, input().split())

MAX = 50 + 10

matrix = [[" "] * (MAX) for _ in range(MAX)]
visited = [[False] * (MAX) for _ in range(MAX)]
cnt = 0


def dfs(x, y):
    visited[x][y] = True

    if matrix[x][y] == "-" and matrix[x][y + 1] == "-":
        dfs(x, y + 1)
    elif matrix[x][y] == "|" and matrix[x + 1][y] == "|":
        dfs(x + 1, y)


for i in range(1, N + 1):
    line = input()
    for j in range(1, M + 1):
        matrix[i][j] = line[j - 1]


# print
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
