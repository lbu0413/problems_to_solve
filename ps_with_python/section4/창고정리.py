N = int(input())
boxes = list(map(int, input().split()))
M = int(input())

box_count = [0] * 101

min_box = float("inf")
max_box = float("-inf")

for i in boxes:
    box_count[i] += 1
    if i > max_box:
        max_box = i

    if i < min_box:
        min_box = i


for _ in range(M):
    if box_count[max_box] == 1:
        box_count[max_box] -= 1
        max_box -= 1
        box_count[max_box] += 1

    else:
        box_count[max_box] -= 1
        box_count[max_box - 1] += 1

    if box_count[min_box] == 1:
        box_count[min_box] -= 1
        min_box += 1
        box_count[min_box] += 1

    else:
        box_count[min_box] -= 1
        box_count[min_box + 1] += 1

print(max_box - min_box)
