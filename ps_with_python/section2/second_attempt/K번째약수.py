import sys

input = sys.stdin.readline

N, K = map(int, input().split())

cd = []

for i in range(1, N + 1):
    if N % i == 0:
        cd.append(i)


if len(cd) < K:
    print(-1)

else:
    print(cd[K - 1])
