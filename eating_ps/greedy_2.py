# boj14247

import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
growth_rate = list(map(int, sys.stdin.readline().split()))
index_arr = [i for i in range(n)]

index_arr = sorted(index_arr, key=lambda x: growth_rate[x])


cnt = 0
for i in range(n):
    index = index_arr[i]
    cnt += trees[index] + i * growth_rate[index]

print(cnt)
