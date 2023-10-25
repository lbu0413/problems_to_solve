import sys

N, K = map(int, input().split())
nums = list(map(int, input().split()))
M = int(input())

ans = []

cnt = 0


def dfs(level):
    global cnt
    if len(ans) == K:
        if sum(ans) % M == 0:
            cnt += 1
    else:
        for i in range(level, N):
            if nums[i] not in ans:
                ans.append(nums[i])
                dfs(i)
                ans.pop()


dfs(0)
print(cnt)
