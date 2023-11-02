N, M = map(int, input().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(M):
    a, b, c = map(int, input().split())
    matrix[a][b] = c


for j in range(1, N + 1):
    for k in range(1, N + 1):
        print(matrix[j][k], end=" ")
    print()
