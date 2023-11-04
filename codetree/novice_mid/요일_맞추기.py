m1, d1, m2, d2 = map(int, input().split())

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1d1 = sum(months[:m1]) + d1
m2d2 = sum(months[:m2]) + d2

diff = m2d2 - m1d1

while diff < 0:
    diff += 7

day = days[diff % 7]
print(day)
