N, M = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
checker = [0] * (N + 1)
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1


def dfs(level):
    global cnt
    if level == N:
        cnt += 1
        for i in path:
            print(i, end=" ")
        print()

    else:
        for i in range(1, N + 1):
            if matrix[level][i] == 1 and checker[i] == 0:
                checker[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                checker[i] = 0


path = []
path.append(1)
checker[1] = 1
dfs(1)
print(cnt)
