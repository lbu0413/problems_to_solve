N = int(input())
M = int(input())


graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(idx):
    global answer
    visited[idx] = True
    answer += 1

    for i in range(1, N + 1):
        if graph[idx][i] == 1 and visited[i] == False:
            dfs(i)


dfs(1)

print(answer - 1)
