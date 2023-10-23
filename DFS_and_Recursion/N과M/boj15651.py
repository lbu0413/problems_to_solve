import sys

input = sys.stdin.readline

N, M = map(int, input().split())
checker = [0] * M


def dfs(level):
    if level == M:
        print(*checker)
    else:
        for i in range(1, N + 1):
            checker[level] = i
            dfs(level + 1)


dfs(0)
