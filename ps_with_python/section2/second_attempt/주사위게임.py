N = int(input())

max_ = float("-inf")

for i in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        prize = 10000 + a * 1000

    elif a == b or a == c:
        prize = 1000 + a * 100

    elif b == c:
        prize = 1000 + b * 100

    else:
        prize = max(a, b, c) * 100

    if prize > max_:
        max_ = prize

print(max_)
