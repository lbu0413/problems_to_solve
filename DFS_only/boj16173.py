import sys

input = sys.stdin.readline

N = int(input())
MAX = 3 + 100 + 10

matrix = [[0] * (MAX) for _ in range(MAX)]
visited = [[False] * (MAX) for _ in range(MAX)]
dirX = [0, 1]
dirY = [1, 0]


def dfs(x, y):
    visited[x][y] = True
    if x == N and y == N:
        return

    for i in range(2):
        newX = x + dirX[i] * matrix[x][y]
        newY = y + dirY[i] * matrix[x][y]
        if not visited[newX][newY]:
            dfs(newX, newY)


for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        matrix[i][j] = row[j - 1]


dfs(1, 1)
print("HaruHaru" if visited[N][N] else "Hing")
