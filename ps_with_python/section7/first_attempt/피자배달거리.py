import sys

input = sys.stdin.readline
N, M = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(N)]
house = []
pizza = []
combined = [0] * M
res = float("inf")


for i in range(N):
    for j in range(N):
        if map_[i][j] == 1:
            house.append((i, j))

        if map_[i][j] == 2:
            pizza.append((i, j))


def dfs(level, start):
    global res

    if level == M:
        sum = 0
        for j in range(len(house)):
            x1 = house[j][0]
            y1 = house[j][1]
            distance = 2147000000

            for x in combined:
                x2 = pizza[x][0]
                y2 = pizza[x][1]
                distance = min(distance, abs(x1 - x2) + abs(y1 - y2))

            sum += distance

        if sum < res:
            res = sum

    else:
        for i in range(start, len(pizza)):
            combined[level] = i
            dfs(level + 1, i + 1)


dfs(0, 0)
print(res)
