import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []


def dfs():
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(1, N + 1):
            if i not in ans:
                ans.append(i)
                dfs()
                ans.pop()


dfs()
