N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []
prev = 0
visited = [False] * N


# 1 7 9 9
def dfs(level):
    global prev

    if len(ans) == M:
        print(*ans)

    else:
        for i in range(level, N):
            if not visited[i] and prev != nums[i]:
                visited[i] = True
                ans.append(nums[i])
                dfs(i + 1)
                prev = nums[i]
                visited[i] = False
                ans.pop()


dfs(0)
