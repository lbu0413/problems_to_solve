N, M = map(int, input().split())
nums = list(map(int, input().split()))


# 1 2 1 3 1 1 1 2

cnt = 0
left = 0
right = 1
total = nums[left]


while True:
    if total < M:
        if right < N:
            total += nums[right]
            right += 1
        else:
            break

    elif total > M:
        total -= nums[left]
        left += 1

    else:
        cnt += 1
        total -= nums[left]
        left += 1

print(cnt)
