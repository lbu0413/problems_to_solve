N, K = map(int, input().split())
nums = list(map(int, input().split()))

sum_ = set()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_.add(nums[i] + nums[j] + nums[k])


sum_ = sorted(list(sum_), reverse=True)
print(sum_[K - 1])
