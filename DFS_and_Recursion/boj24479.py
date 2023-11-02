import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


N, M, R = map(int, input().split())

visited = [False] * (N + 1)
matrix = [[] for _ in range(N + 1)]
order = 1
answer = [0] * (N + 1)


# filling in numbers to the matrix
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

# sort each array in the matrix
for i in range(1, N + 1):
    matrix[i] = sorted(matrix[i])


# dfs function
def dfs(idx):
    global visited, matrix, order, answer
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in matrix[idx]:
        if not visited[i]:
            dfs(i)


# dfs call
dfs(R)

for i in range(1, N + 1):
    print(answer[i])
