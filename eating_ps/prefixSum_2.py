# boj2015

import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


psum = [0] * N
psum[0] = nums[0]


for i in range(1, N):
    psum[i] = psum[i - 1] + nums[i]


answer = 0
count = {}


for i in range(N):
    goal = psum[i] - K

    if goal in count:
        answer += count[goal]

    if goal == 0:
        answer += 1

    if psum[i] not in count:
        count[psum[i]] = 0

    count[psum[i]] += 1

print(answer)


# goal: 5
# nums = 1 2 3 4 5 0
# psum = 1 3 6 10 15 15
