# boj1300


#  my first solution which failed
#  메모리 복잡도가 너무 높아져버려서 풀 수 없다.

# n = int(input())
# k = int(input())

# A = [[0] * n] * n
# B = []
# for i in range(n):
#     for j in range(n):
#         A[i][j] = (i+1) * (j+1)
#         B.append(A[i][j])
# B.sort()

# print(B[k])


# 만약 x가 어떤 배열에서 k번째로 작은 수라면,
# x보다 작은 수가 k-1개 이하 있다
# x보다 작은 수가 n-k개 이하 있다

# 예를 들어 배열 A가 있다
# A = [1, 1, 2, 3, 3, 6, 7, 7, 8, 9, 9, 10, 10, 10, 15, 17]
# 작은 수 0  0  2  3  3  5  6  6  8  9  9  11  11  11  14  15
# 큰 수  14 14 13 11 11 10 8  8  7  5  5   2   2   2   1   0


# 만약 X가 어떤 배열에서 13번째로 작은 수라면,
# X보다 작은 수가 12개 이하 있고
# X보다 큰 수가 3 개 이하 있다


n = int(input())
k = int(input())

# n개가 주어졌을 때, k번째 수를 찾아야 한다.
# B라는 배열의 k번째를 찾아야하는데
# k번째 보다 작은 수는 k-1 이하가 있을 것이고
# k번째 보다 큰 수는 n-k 이하가 있을 것이다


def get_nums_smaller(num):
    num_counter = 0
    # K번째 수 보다 작은 수가 얼마나 있는지 계산하는 함수
    for i in range(1, n + 1):
        num_counter += min(n, (num - 1) // i)
    return num_counter


def get_nums_greater(num):
    # K번째 수 보다 큰 수가 얼마나 있는지 계산하는 함수
    num_counter = 0
    for i in range(1, n + 1):
        num_counter += n - min(n, num // i)
    return num_counter


low = 1
high = n * n
answer = -1

while low <= high:
    mid = (low + high) // 2

    num_smaller = get_nums_smaller(mid)
    num_greater = get_nums_greater(mid)

    if num_smaller > k - 1:
        high = mid - 1

    elif num_greater > n * n - k:
        low = mid + 1

    else:
        answer = mid
        break

print(answer)
