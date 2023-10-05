import sys

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for i in range(n)]

nums.sort()


def difference(a, b, c):
    return abs(a + b + c - b * 3)


answer = -1
for i in range(1, n - 1):
    answer = max(answer, difference(nums[0], nums[i], nums[i + 1]))
    answer = max(answer, difference(nums[i - 1], nums[i], nums[n - 1]))

print(answer)
