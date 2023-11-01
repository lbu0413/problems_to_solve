import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

total = 0
tmp = 0

for x in scores:
    if x == 1:
        tmp += 1

    if x == 0:
        tmp = 0

    total += tmp

print(total)
