import sys

sys.setrecursionlimit(10**6)


def dfs(idx):
    global visited, graph
    visited[idx] = True
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())

MAX = 1000 + 10

graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = True
    graph[v][u] = True


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
