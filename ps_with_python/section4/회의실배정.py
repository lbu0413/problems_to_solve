N = int(input())

schedule = []

for i in range(N):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule.sort(key=lambda x: x[1])


current = (0, 0)
cnt = 0
for start, end in schedule:
    if start >= current[1]:
        cnt += 1
        current = (start, end)

print(cnt)
