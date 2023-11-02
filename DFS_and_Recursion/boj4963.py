import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dirX = [-1, -1, -1, 0, 1, 1, 1, 0]  # col
dirY = [-1, 0, 1, 1, 1, 0, -1, -1]  # row


def dfs(y, x):
    global cnt
    matrix[y][x] = False

    for i in range(8):
        newX = x + dirX[i]
        newY = y + dirY[i]
        if matrix[newY][newX]:
            dfs(newY, newX)


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    MAX = 50 + 10

    matrix = [[False] * (MAX) for _ in range(MAX)]

    # matrix info fill
    for i in range(1, H + 1):
        row = list(map(int, input().split()))
        for j in range(1, W + 1):
            matrix[i][j] = row[j - 1] == 1

    # print
    cnt = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if matrix[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
