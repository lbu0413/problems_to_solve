N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
visited = [False] * N


def dfs():
    prev = 0
    if len(ans) == M:
        print(*ans)

    else:
        for i in range(N):
            if not visited[i] and prev != nums[i]:
                visited[i] = True
                ans.append(nums[i])
                prev = nums[i]
                dfs()
                visited[i] = False
                ans.pop()


dfs()
