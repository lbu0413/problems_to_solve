import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []


def dfs(level):
    if len(ans) == M:
        print(*ans)

    else:
        for i in range(level, N):
            if nums[i] not in ans:
                ans.append(nums[i])
                dfs(i + 1)
                ans.pop()


dfs(0)
