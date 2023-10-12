N = int(input())

profiles = []
for i in range(N):
    height, weight = map(int, input().split())
    profiles.append((height, weight))

profiles.sort(reverse=True)

compare = 0
cnt = 0


for height, weight in profiles:
    if weight > compare:
        cnt += 1
        compare = weight

print(cnt)
