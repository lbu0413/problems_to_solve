N = int(input())
scores = list(map(int, input().split()))


total = 0
checker = 0

for i in scores:
    if i == 1:
        checker += 1

    else:
        checker = 0

    total += checker

print(total)
