import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def reverse(x):
    reversed_num = ""

    while x > 0:
        reversed_num += str(x % 10)
        x //= 10

    return int(reversed_num)


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


for x in nums:
    reversed_ = reverse(x)
    if isPrime(reversed_):
        print(reversed_, end=" ")
