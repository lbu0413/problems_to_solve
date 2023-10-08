N = int(input())
nums = list(map(int, input().split()))


def digit_sum(x):
    add = 0
    while x != 0:
        add += x % 10
        x //= 10
    return add


max = 0
for i in range(N):
    if digit_sum(nums[i]) > max:
        max = digit_sum(nums[i])
        answer = nums[i]

    elif digit_sum(nums[i]) == max:
        continue

print(answer)
