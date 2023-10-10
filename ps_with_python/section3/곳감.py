N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

M = int(input())

for i in range(M):
    row, direction, num = map(int, input().split())
    for j in range(num):
        if direction == 0:
            board[row - 1].append(board[row - 1].pop(0))
        else:
            board[row - 1].insert(0, board[row - 1].pop())


res = 0
a = 0
b = N - 1
for i in range(N):
    for j in range(a, b + 1):
        res += board[i][j]
    if i < N // 2:
        a += 1
        b -= 1
    else:
        a -= 1
        b += 1

print(res)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4
