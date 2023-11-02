board = [list(map(int, input().split())) for _ in range(7)]


cnt = 0
for i in range(7):
    for j in range(3):
        tmp = board[i][j : j + 5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(5 // 2):
            if board[j + k][i] != board[j + 5 - k - 1][i]:
                break
        else:
            cnt += 1

print(cnt)

# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
