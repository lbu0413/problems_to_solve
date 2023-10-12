K, N = map(int, input().split())

wires = [int(input()) for _ in range(K)]


left = 0
right = max(wires)


def cutting_wires(cut):
    cnt = 0
    for wire in wires:
        cnt += wire // cut

    return cnt


while left <= right:
    mid = (left + right) // 2

    if cutting_wires(mid) == N:
        print(mid)
        break

    elif cutting_wires(mid) > N:
        left = mid + 1

    else:
        right = mid - 1
