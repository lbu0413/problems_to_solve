import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []


def dfs():
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(N):
            ans.append(nums[i])
            dfs()
            ans.pop()


dfs()
