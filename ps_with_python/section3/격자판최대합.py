import sys

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


row_sum, col_sum, diagonal_left, diagonal_right = 0, 0, 0, 0
first_max = 0
for i in range(N):
    for j in range(N):
        row = board[i][j]
        col = board[j][i]

    row_sum += row
    col_sum += col

    first_max = max(first_max, row_sum, col_sum)

    diagonal_left += board[i][i]
    diagonal_right += board[i][N - i - 1]


print(max(first_max, diagonal_left, diagonal_right))
