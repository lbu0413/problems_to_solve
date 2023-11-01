import sys

input = sys.stdin.readline
N = int(input())

checker = [0] * (N + 1)
cnt = 0

for i in range(2, N + 1):
    if checker[i] == 0:
        cnt += 1
        for j in range(i, N + 1, i):
            checker[j] = 1

print(cnt)
