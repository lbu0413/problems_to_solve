N, M = map(int, input().split())

cnt = [0] * M
total = 0


def dfs(idx):
    global total
    if idx == M:
        for i in range(M):
            print(cnt[i], end=" ")
        total += 1
        print()
    else:
        for i in range(1, N + 1):
            cnt[idx] = i
            dfs(idx + 1)


dfs(0)
print(total)
