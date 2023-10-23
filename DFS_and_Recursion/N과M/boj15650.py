import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []


def dfs(level):
    if len(ans) == M:
        print(*ans)

    else:
        for i in range(level, N + 1):
            if i not in ans:
                ans.append(i)
                dfs(i + 1)
                ans.pop()


dfs(1)
