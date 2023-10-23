import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []


def dfs(start):
    if len(ans) == M:
        print(*ans)

    else:
        for i in range(start, N + 1):
            ans.append(i)
            dfs(i)
            ans.pop()


dfs(1)
