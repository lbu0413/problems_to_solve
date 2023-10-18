N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
M = int(input())


total = float("inf")


def dfs(level, current):
    global total
    if current > M:
        return

    if level > total:
        return

    if current == M:
        if level < total:
            total = level

    else:
        for i in range(N):
            dfs(level + 1, current + coins[i])


dfs(0, 0)
print(total)
