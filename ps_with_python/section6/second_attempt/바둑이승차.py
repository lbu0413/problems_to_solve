import sys

input = sys.stdin.readline

C, N = map(int, input().split())

weights = [int(input()) for _ in range(N)]
visited = [0] * N
total = sum(weights)
max_ = float("-inf")


def dfs(v, cur, tot):
    global max_
    if cur > C:
        return

    if cur + (total - tot) < max_:
        return

    if v == N:
        if cur > max_:
            max_ = cur

    else:
        dfs(v + 1, cur + weights[v], tot + weights[v])
        dfs(v + 1, cur, tot + weights[v])


dfs(0, 0, 0)
print(max_)
