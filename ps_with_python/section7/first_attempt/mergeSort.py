arr = [23, 11, 45, 36, 15, 67, 33, 21]


def merge_sort(left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(left, mid)
        merge_sort(mid + 1, right)

        p1 = left
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= right:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1

            else:
                tmp.append(arr[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + arr[p1 : mid + 1]

        if p2 <= right:
            tmp = tmp + arr[p2 : right + 1]

        for i in range(len(tmp)):
            arr[left + i] = tmp[i]


print(arr)
merge_sort(0, 7)
print(arr)
