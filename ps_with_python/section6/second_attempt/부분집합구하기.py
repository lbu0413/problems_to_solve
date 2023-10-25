import sys

input = sys.stdin.readline
N = int(input())


checker = [0] * (N + 1)


def dfs(v):
    if v > N:
        for i in range(1, N + 1):
            if checker[i] == 1:
                print(i, end=" ")
        print()
    else:
        checker[v] = 1
        dfs(v + 1)
        checker[v] = 0
        dfs(v + 1)


dfs(1)
