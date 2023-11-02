import sys
import itertools as it

N, F = map(int, input().split())
printer = [1] * N

for i in range(1, N):
    printer[i] = printer[i - 1] * (N - i) // i

nums = list(range(1, N + 1))

for tmp in it.permutations(nums):
    sum = 0
    for idx, x in enumerate(tmp):
        sum += x * printer[idx]
    if sum == F:
        for x in tmp:
            print(x, end=" ")
        break
