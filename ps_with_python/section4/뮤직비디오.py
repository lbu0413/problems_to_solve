N, M = map(int, input().split())
tracks = list(map(int, input().split()))


left = 1
right = sum(tracks)


def putting_tracks(storage):
    cnt = 1
    size = 0
    for i in tracks:
        if size + i > storage:
            cnt += 1
            size = i

        else:
            size += i

    return cnt


ans = 0
while left <= right:
    mid = (left + right) // 2
    if putting_tracks(mid) <= M:
        ans = mid
        right = mid - 1

    else:
        left = mid + 1


print(ans)
