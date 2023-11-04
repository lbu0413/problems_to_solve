N = int(input())


def recursion(N):
    if N < 10:
        return N * N

    x = N % 10
    return recursion(N // 10) + x * x


print(recursion(N))
