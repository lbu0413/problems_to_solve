import sys

input = sys.stdin.readline
N = int(input())
coins = []

three = [0] * 3

min_ = float("inf")

for i in range(N):
    coin = int(input())
    coins.append(coin)


def dfs(level):
    global min_
    if level == N:
        tmp = set(three)
        if len(tmp) == 3:
            sub = max(three) - min(three)
            if sub < min_:
                min_ = sub

    else:
        for i in range(3):
            three[i] += coins[level]
            dfs(level + 1)
            three[i] -= coins[level]


dfs(0)
print(min_)
