import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dirX = [0, 0, -1, 1]
dirY = [1, -1, 0, 0]


def dfs(y, x):
    global visited, matrix, cnt

    visited[y][x] = True

    for i in range(4):
        newX = x + dirX[i]
        newY = y + dirY[i]
        if matrix[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


T = int(input())
MAX = 50 + 10

# TC
while T > 0:
    T -= 1
    M, N, K = map(int, input().split())
    cnt = 0

    matrix = [[False] * (MAX) for _ in range(MAX)]
    visited = [[False] * (MAX) for _ in range(MAX)]

    # matrix info
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y + 1][x + 1] = True

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if not visited[i][j] and matrix[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
