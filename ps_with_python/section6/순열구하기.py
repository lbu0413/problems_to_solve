N, M = map(int, input().split())

checker = [0] * (N + 1)
printer = [0] * M
cnt = 0


def dfs(idx):
    global cnt
    if idx == M:
        for j in range(M):
            print(printer[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, N + 1):
            if checker[i] == 0:
                printer[idx] = i
                checker[i] = 1
                dfs(idx + 1)
                checker[i] = 0


dfs(0)
print(cnt)
