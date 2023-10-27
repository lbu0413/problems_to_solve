N = int(input())
nums = list(map(int, input().split()))
S = sum(nums)
ans = set()


def dfs(level, current):
    if level == N:
        if current > 0:
            ans.add(current)

    else:
        dfs(level + 1, current + nums[level])
        dfs(level + 1, current - nums[level])
        dfs(level + 1, current)


dfs(0, 0)
print(S - len(ans))
