import sys

N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
change = int(input())


min_ = float("inf")


def dfs(level, cur):
    global min_

    if level > min_:
        return

    if cur > change:
        return

    if cur == change:
        if level < min_:
            min_ = level
    else:
        for i in range(N):
            dfs(level + 1, cur + coins[i])


dfs(0, 0)
print(min_)
