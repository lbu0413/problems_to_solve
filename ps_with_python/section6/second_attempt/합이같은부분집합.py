import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sum_ = sum(nums)


def dfs(level, current):
    global sum_

    if current > sum_ // 2:
        return

    if level == N:
        if current == sum_ - current:
            print("YES")
            sys.exit(0)

    else:
        dfs(level + 1, current + nums[level])
        dfs(level + 1, current)


dfs(0, 0)
print("NO")
