N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []


def dfs(level):
    if len(ans) == M:
        print(*ans)
        return
    prev = 0
    for i in range(level, N):
        if prev != nums[i]:
            ans.append(nums[i])
            prev = nums[i]
            dfs(i)
            ans.pop()


dfs(0)
