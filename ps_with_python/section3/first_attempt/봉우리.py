N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

first_row = [0] * N
last_row = [0] * N
board.insert(0, first_row)
board.append(last_row)

for i in range(len(board)):
    board[i].insert(0, 0)
    board[i].append(0)

summits = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if (
            board[i][j] > board[i - 1][j]
            and board[i][j] > board[i + 1][j]
            and board[i][j] > board[i][j - 1]
            and board[i][j] > board[i][j + 1]
        ):
            summits += 1

        else:
            continue

print(summits)
