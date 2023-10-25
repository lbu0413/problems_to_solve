N, M = map(int, input().split())


ans = [[0] * N for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    ans[a - 1][b - 1] = c


for i in range(N):
    print(ans[i])
