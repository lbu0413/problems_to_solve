N, M = map(int, input().split())
tracks = list(map(int, input().split()))


left = 1
right = sum(tracks)


def putting_tracks(storage):
    cnt = 0
    size = 0
    for i in range(N):
        size += tracks[i]
        if size > storage:
            cnt += 1
            size = tracks[i]

        elif size == storage:
            cnt += 1
            size = 0
    return cnt


while left <= right:
    mid = (left + right) // 2
    if putting_tracks(mid) == M:
        print(mid)
        break

    elif putting_tracks(mid) < M:
        right = mid - 1

    else:
        left = mid + 1
