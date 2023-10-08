N, S = map(int, input().split())
nums = list(map(int, input().split()))

from itertools import combinations


cnt = 0
for i in range(N):
    nums_combination = list(combinations(nums, i + 1))
    for j in nums_combination:
        if sum(j) == S:
            cnt += 1

print(cnt)
