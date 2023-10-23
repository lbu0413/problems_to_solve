import sys

input = sys.stdin.readline

N, M = map(int, input().split())

checker = [0] * (N + 1)
ans = [0] * M


def dfs(level):
    if level == M:
        for i in ans:
            print(i, end=" ")
        print()

    else:
        for i in range(1, N + 1):
            if checker[i] == 0:
                checker[i] = 1
                ans[level] = i
                dfs(level + 1)
                checker[i] = 0


dfs(0)
