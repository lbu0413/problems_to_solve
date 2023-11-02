TC = 10

cards = [i for i in range(21)]

for i in range(TC):
    a, b = map(int, input().split())
    inc = 0
    for j in range(a, (a + b) // 2 + 1):
        cards[j], cards[b - inc] = cards[b - inc], cards[j]
        inc += 1

print(" ".join(map(str, cards[1:])))
