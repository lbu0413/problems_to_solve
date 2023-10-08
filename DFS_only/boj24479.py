import sys

sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)
order = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N + 1):
    graph[i] = sorted(graph[i])


def dfs(idx):
    global order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


dfs(R)

for i in range(1, N + 1):
    print(answer[i])
