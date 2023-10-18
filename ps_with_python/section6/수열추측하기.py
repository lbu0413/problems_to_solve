import sys

N, F = map(int, input().split())

binary = [1] * (N)
checker = [0] * (N + 1)
printer = [0] * N


def dfs(idx, current):
    if idx == N and current == F:
        for i in printer:
            print(i, end=" ")
        sys.exit(0)

    else:
        for j in range(1, N + 1):
            if checker[j] == 0:
                printer[idx] = j
                checker[j] = 1
                dfs(idx + 1, current + printer[idx] * binary[idx])
                checker[j] = 0


for i in range(1, N):
    binary[i] = binary[i - 1] * (N - i) // i

dfs(0, 0)
