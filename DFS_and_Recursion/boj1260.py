from collections import deque
import sys

input = sys.stdin.readline


N, M, V = map(int, input().split())

matrix = [[False] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)


for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = True
    matrix[y][x] = True


def dfs(idx):
    global order, visited, matrix, answer
    visited[idx] = True
    print(idx, end=" ")

    for i in range(1, N + 1):
        if not visited[i] and matrix[idx][i]:
            dfs(i)


def bfs():
    q = deque([])
    q.append(V)
    visited[V] = True

    while q:
        idx = q.popleft()
        print(idx, end=" ")

        for i in range(1, N + 1):
            if not visited[i] and matrix[idx][i]:
                q.append(i)
                visited[i] = True


dfs(V)
print()
visited = [False] * (N + 1)
bfs()
