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
            ans.append(nums[i])
            dfs(i)
            ans.pop()


dfs(0)
