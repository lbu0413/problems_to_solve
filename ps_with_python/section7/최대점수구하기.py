import sys

input = sys.stdin.readline

N, M = map(int, input().split())
points_arr = []
time_arr = []
total = 0

for i in range(N):
    points, time = map(int, input().split())
    points_arr.append(points)
    time_arr.append(time)


def dfs(level, current, limit):
    global total

    if limit > M:
        return

    if level == N:
        if current > total:
            total = current

    else:
        dfs(level + 1, current + points_arr[level], limit + time_arr[level])
        dfs(level + 1, current, limit)


dfs(0, 0, 0)
print(total)
