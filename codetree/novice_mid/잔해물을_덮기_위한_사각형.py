OFFSET = 1000
MAX = OFFSET * 2 + 1

map_ = [[0] * MAX for _ in range(MAX)]


for i in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            map_[j + OFFSET][k + OFFSET] = i


area_found = False
minX, minY, maxX, maxY = MAX, MAX, 0, 0
for i in range(MAX):
    for j in range(MAX):
        if map_[i][j] == 1:
            area_found = True
            minX = min(minX, i)
            minY = min(minY, j)
            maxX = max(maxX, i)
            maxY = max(maxY, j)

if area_found:
    area = (maxX - minX + 1) * (maxY - minY + 1)
else:
    area = 0


print(area)
