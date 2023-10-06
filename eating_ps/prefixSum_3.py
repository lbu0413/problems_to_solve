import sys

N, M = map(int, sys.stdin.readline().split())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


psum = [[0] * M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            psum[i][j] = nums[i][j]

        elif i == 0 and j != 0:
            psum[i][j] = psum[i][j - 1] + nums[i][j]

        elif i != 0 and j == 0:
            psum[i][j] = psum[i - 1][j] + nums[i][j]

        else:
            psum[i][j] = (
                psum[i][j - 1] + psum[i - 1][j] - psum[i - 1][j - 1] + nums[i][j]
            )


K = int(sys.stdin.readline())
answer = 0
for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == 1 and b == 1:
        answer = psum[c - 1][d - 1]

    elif a == 1 and b != 1:
        answer = psum[c - 1][d - 1] - psum[c - 1][b - 2]

    elif a != 1 and b == 1:
        answer = psum[c - 1][d - 1] - psum[a - 2][d - 1]

    else:
        answer = (
            psum[c - 1][d - 1]
            - psum[c - 1][b - 2]
            - psum[a - 2][d - 1]
            + psum[a - 2][b - 2]
        )

    print(answer)
