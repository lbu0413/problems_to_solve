import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []


def dfs():
    if len(ans) == M:
        for i in ans:
            print(i, end=" ")
        print()
    else:
        for i in nums:
            if i not in ans:
                ans.append(i)
                dfs()
                ans.pop()


dfs()
