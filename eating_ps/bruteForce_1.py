# boj10819

# N개의 길이의 숫자들이 주어졌을 때, 순열의 갯수는 N! 이다.
# 예를 들어 3 5 7 이 주어졌을때, 모든 3 5 7의 순열은 3! => 6이다.

# from itertools import permutations

# N = int(input())
# nums = list(map(int, input().split()))

# perm_nums = list(permutations(nums))
# max_num = 0
# for perm_num in perm_nums:
#     sum_num = 0
#     for j in range(1, len(perm_num)):
#         sum_num += abs(perm_num[j - 1] - perm_num[j])
#     if sum_num > max_num:
#         max_num = sum_num

# print(max_num)


from itertools import permutations

N = int(input())
a = list(map(int, input().split()))

ans = -1
for p in list(permutations(a)):
    sum = 0
    for i in range(N - 1):
        sum += abs(p[i] - p[i + 1])

    if ans < sum:
        ans = sum

print(ans)
