# boj 11659

import sys

# N, M = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# psum = nums
# for i in range(N):
#     if i == 0:
#         continue
#     psum[i] = psum[i - 1] + nums[i]


# for k in range(M):
#     i, j = map(int, sys.stdin.readline().split())
#     j = j - 1
#     i = i - 2
#     if i < 0:
#         print(psum[j])
#     else:
#         print(psum[j] - psum[i])


#  선생님 솔루션

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

psum = [0] * N
psum[0] = nums[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + nums[i]


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        answer = psum[b - 1]
    else:
        answer = psum[b - 1] - psum[a - 2]

    print(answer)
