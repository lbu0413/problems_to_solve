import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * M
total = 0


def dfs(level):
    global total
    if level == M:
        for i in range(M):
            print(visited[i], end=" ")
        print()
        total += 1

    else:
        for i in range(1, N + 1):
            visited[level] = i
            dfs(level + 1)


dfs(0)
print(total)
