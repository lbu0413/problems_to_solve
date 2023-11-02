N = int(input())
a, b = map(int, input().split())
M = int(input())

matrix = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = -1


for i in range(M):
    c, d = map(int, input().split())
    matrix[c].append(d)
    matrix[d].append(c)

for j in range(1, N + 1):
    matrix[j] = sorted(matrix[j])


def dfs(idx, count):
    global answer
    visited[idx] = True
    if idx == b:
        answer = count
        return

    for i in range(1, N + 1):
        if i in matrix[idx] and not visited[i]:
            dfs(i, count + 1)


dfs(a, 0)
print(answer)
