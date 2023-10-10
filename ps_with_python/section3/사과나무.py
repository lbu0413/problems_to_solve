# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
import sys

N = int(sys.stdin.readline())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

harvest = 0

a = b = N // 2


for i in range(N):
    for j in range(a, b + 1):
        harvest += field[i][j]
    if i < N // 2:
        a -= 1
        b += 1
    else:
        a += 1
        b -= 1


print(harvest)
