N = int(input())
nums = list(map(int, input().split()))


def reverse(x):
    newNum = ""
    while x != 0:
        num_part = x % 10
        if num_part == 0:
            newNum += ""
        else:
            newNum += str(num_part)
        x //= 10
    return newNum


def isPrime(x):
    x = int(x)
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


for i in nums:
    reversed_num = reverse(i)
    if isPrime(reversed_num):
        print(reversed_num, end=" ")
