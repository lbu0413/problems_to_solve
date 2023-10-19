N, M = map(int, input().split())
res = [0] * (N + 1)
cnt = 0


def dfs(level, start):
    global cnt
    if level == M:
        for i in range(M):
            print(res[i], end=" ")
        cnt += 1
        print()

    else:
        for j in range(start, N + 1):
            res[level] = j
            dfs(level + 1, start + j)


dfs(0, 1)
print(cnt)
