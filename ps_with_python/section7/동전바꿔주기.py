import sys

input = sys.stdin.readline

T = int(input())
K = int(input())

ct = []
cn = []
cnt = 0

for i in range(K):
    a, b = map(int, input().split())
    ct.append(a)
    cn.append(b)


def dfs(level, current):
    global cnt

    if current > T:
        return

    if level == K:
        if current == T:
            cnt += 1

    else:
        for i in range(cn[level] + 1):
            dfs(level + 1, current + ct[level] * i)


dfs(0, 0)
print(cnt)
