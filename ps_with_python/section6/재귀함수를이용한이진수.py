N = int(input())


def DFS(N):
    if N == 0:
        return
    else:
        DFS(N // 2)
        print(N % 2, end="")


print(DFS(N))
