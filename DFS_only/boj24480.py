import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [False] * (N + 1)
matrix = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
order = 1

# matrix info add
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)


# matrix sort
for i in range(1, N + 1):
    matrix[i] = sorted(matrix[i], reverse=True)


# define dfs
def dfs(idx):
    global order, ans, visited, matrix

    visited[idx] = True
    ans[idx] = order
    order += 1

    for i in matrix[idx]:
        if not visited[i]:
            dfs(i)


# dfs call
dfs(R)

# print ans
for i in range(1, N + 1):
    print(ans[i])
