T = int(input())


for i in range(T):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_part = sorted(nums[s - 1 : e])
    kth_num = nums_part[k - 1]
    print(f"#{i+1} {kth_num}")
