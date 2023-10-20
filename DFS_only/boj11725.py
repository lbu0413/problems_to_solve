import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
matrix = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)

for i in range(N - 1):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)


def dfs(idx):
    global visited, answer, matrix
    visited[idx] = True

    for i in matrix[idx]:
        if not visited[i]:
            answer[i] = idx
            dfs(i)


dfs(1)
for i in range(2, N + 1):
    print(answer[i])
