import sys

input = sys.stdin.readline

code = list(map(int, input().strip()))
N = len(code)
res = [0] * (N + 3)
code.insert(N, -1)
cnt = 0


def dfs(level, pos):
    global cnt
    if level == N:
        cnt += 1
        for i in range(pos):
            print(chr(res[i] + 64), end="")
        print()

    else:
        for i in range(1, 27):
            if i == code[level]:
                res[pos] = i
                dfs(level + 1, pos + 1)

            elif i >= 10 and i // 10 == code[level] and i % 10 == code[level + 1]:
                res[pos] = i
                dfs(level + 2, pos + 1)


dfs(0, 0)
print(cnt)
