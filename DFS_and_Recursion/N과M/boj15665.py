N, M = map(int, input().split())
nums = sorted((list(map(int, input().split()))))
ans = []
prev = 0


def dfs():
    if len(ans) == M:
        print(*ans)
        return
    prev = 0
    for i in range(N):
        if prev != nums[i]:
            ans.append(nums[i])
            prev = nums[i]
            dfs()
            ans.pop()


dfs()
