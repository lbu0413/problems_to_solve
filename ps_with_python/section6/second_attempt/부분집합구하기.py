import sys

input = sys.stdin.readline

N = int(input())
answer = [0] * (N + 1)


def dfs(level):
    if level > N:
        for i in range(1, N + 1):
            if answer[i] == 1:
                print(i, end=" ")
        print()
    else:
        answer[level] = 1
        dfs(level + 1)
        answer[level] = 0
        dfs(level + 1)


dfs(1)
