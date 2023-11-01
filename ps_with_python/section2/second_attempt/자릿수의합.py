import sys

input = sys.stdin.readline
max_ = float("-inf")


def digit_sum(x):
    sum_ = 0
    tmp = x
    while tmp > 0:
        sum_ += tmp % 10
        tmp = tmp // 10
    return [sum_, x]


N = int(input())
nums = list(map(int, input().split()))

for i in nums:
    cur = digit_sum(i)
    if cur[0] > max_:
        max_ = cur[0]
        ans = cur[1]

print(ans)
