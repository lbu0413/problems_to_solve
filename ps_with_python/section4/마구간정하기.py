house, horse = map(int, input().split())

position = [int(input()) for _ in range(house)]
position.sort()


left = 1
right = max(position)


def calculate(distance):
    cnt = 1
    house_point = position[0]
    for i in range(1, len(position)):
        if position[i] - house_point < distance:
            continue
        else:
            cnt += 1
            house_point = position[i]

    return cnt


final_distance = 0

while left <= right:
    mid = (left + right) // 2
    if calculate(mid) >= horse:
        final_distance = mid
        left = mid + 1
    else:
        right = mid - 1

print(final_distance)
