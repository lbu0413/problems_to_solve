N, K = map(int, input().split())
nums = list(map(int, input().split()))
M = int(input())

cnt = 0


def dfs(level, start, total):
    global cnt
    if level == K:
        if total % M == 0:
            cnt += 1

    else:
        for j in range(start, N):
            dfs(level + 1, j + 1, total + nums[j])


dfs(0, 0, 0)
print(cnt)
