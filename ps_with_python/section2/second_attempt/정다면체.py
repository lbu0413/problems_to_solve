import sys

input = sys.stdin.readline

N, M = map(int, input().split())

checker = {}

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if i + j in checker:
            checker[i + j] += 1
        else:
            checker[i + j] = 1
print(checker)

max_ = max(checker.values())

for key in checker.keys():
    if checker[key] == max_:
        print(key, end=" ")
