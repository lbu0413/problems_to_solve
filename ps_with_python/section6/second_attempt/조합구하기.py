N, M = map(int, input().split())

ans = []
cnt = 0


def dfs(level):
    global cnt
    if len(ans) == M:
        print(*ans)
        cnt += 1
        return

    for i in range(level, N + 1):
        if i not in ans:
            ans.append(i)
            dfs(i)
            ans.pop()


dfs(1)
print(cnt)
