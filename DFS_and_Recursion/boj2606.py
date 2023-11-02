N = int(input())
M = int(input())

matrix = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0


for i in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = True
    matrix[y][x] = True


def dfs(idx):
    global cnt
    visited[idx] = 1
    cnt += 1

    for i in range(1, N + 1):
        if not visited[i] and matrix[idx][i]:
            dfs(i)


dfs(1)
print(cnt - 1)
