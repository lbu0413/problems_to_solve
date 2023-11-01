import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = sorted(nums[s - 1 : e])
    print(f"#{i+1} {ans[k-1]}")
    print()
