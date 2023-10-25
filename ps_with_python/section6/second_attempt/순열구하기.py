import sys

input = sys.stdin.readline

N, M = map(int, input().split())
total = 0

ans = []


def dfs():
    global total

    if len(ans) == M:
        print(*ans)
        total += 1
        return

    for i in range(1, N + 1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()


dfs()
print(total)
