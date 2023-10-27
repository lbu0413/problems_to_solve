import sys

input = sys.stdin.readline

N, M = map(int, input().split())

points = []
time = []

max_ = 0

for i in range(N):
    a, b = map(int, input().split())
    points.append(a)
    time.append(b)


def dfs(level, p, t):
    global max_
    if t > M:
        return

    if level == N:
        if p > max_:
            max_ = p

    else:
        dfs(level + 1, p + points[level], t + time[level])
        dfs(level + 1, p, t)


dfs(0, 0, 0)
print(max_)
