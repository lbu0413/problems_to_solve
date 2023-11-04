N = int(input())

nums = list(map(int, input().split()))


def lcm(a, b):
    gcd = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return a * b // gcd


def lcm_final(idx):
    if idx == 0:
        return nums[0]

    return lcm(lcm_final(idx - 1), nums[idx - 1])


print(lcm_final(N))
