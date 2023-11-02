import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M, N = map(int, input().split())

MAX = 1000 + 10

matrix = [[False] * (MAX) for _ in range(MAX)]


for i in range(1, M + 1):
    row = input()
    for j in range(1, N + 1):
        matrix[i][j] = row[j - 1] == "0"

dirX = [-1, 1, 0, 0]
dirY = [0, 0, -1, 1]


def dfs(x, y):
    global answer
    matrix[x][y] = False
    if x == M:
        answer = True
        return

    for i in range(4):
        newX = x + dirX[i]
        newY = y + dirY[i]
        if matrix[newX][newY]:
            dfs(newX, newY)


# dfs call
answer = False
for j in range(1, N + 1):
    if matrix[1][j]:
        dfs(1, j)

print("YES" if answer else "NO")
