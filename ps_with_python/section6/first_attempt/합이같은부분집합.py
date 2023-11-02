import sys

N = int(input())
nums = list(map(int, input().split()))
total = sum(nums)


def dfs(idx, current):
    if current > (total // 2):
        return

    if idx == N:
        if current == (total - current):
            print("YES")
            sys.exit(0)

    else:
        dfs(idx + 1, current + nums[idx])
        dfs(idx + 1, current)


dfs(0, 0)
print("NO")
