# boj 3090


# 각 순열의 차이의 최댓값을 X 이하로 만들기 위해 연산이 적어도 몇개가 필요한가?
# 위 질문에 대한 알고리즘
# X가 3이라고 했을 때
# a = [10, 6, 5, 1, 9, 7, 2, 3, 10, 5, 3]
# 1. 왼쪽에서 오른쪽으로 일단 순열을 보고 오른쪽의 숫자가 왼쪽보다 3보다 더 많이 차이날 경우, 숫자를 줄여준다
#    그렇게 되면 a = [10, 6, 5, 1, 4, 7, 2, 3, 6, 5, 3] 이 된다.
# 2. 이번에는 오른쪽에서 왼쪽으로 순열을 살펴보면서 왼쪽 숫자가 오른쪽보다 3보다 더 많이 차이날 경우, 숫자를 줄여준다.
#    그렇게 해서 최종족으로 배열은 a = [9, 6, 4, 1, 4, 5, 2, 3, 6, 5, 3] 이렇게 된다.
#    이렇게 왼쪽에서 오른쪽으로 그리고 오른쪽에서 왼쪽으로 순열을 검사하면서 돌렸을 때 모든 순열의 차이는 X보다 이하가 된다.
# 위 예시를 들어 계산하게 되면 총 13번의 연산이 필요하게 된다.


n, t = map(int, input().split())
arr = list(map(int, input().split()))


def needed_num_operation(x):
    arrB = [arr[i] for i in range(n)]  # 임시 배열을 만듬.

    num_operation = 0
    for i in range(n - 1):
        if arrB[i] + x < arrB[i + 1]:
            num_operation += arrB[i + 1] - arrB[i] - x
            arrB[i + 1] = arrB[i] + x

    for i in range(n - 1, 0, -1):
        if arrB[i] + x < arrB[i - 1]:
            num_operation += arrB[i - 1] - arrB[i] - x
            arrB[i - 1] = arrB[i] + x

    return num_operation


left = 0
right = max(arr)
answer = -1

while left <= right:
    mid = (left + right) // 2

    if needed_num_operation(mid) <= t:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1


for i in range(n - 1):
    if arr[i] + answer < arr[i + 1]:
        arr[i + 1] = arr[i] + answer


for i in range(n - 1, 0, -1):
    if arr[i] + answer < arr[i - 1]:
        arr[i - 1] = arr[i] + answer


print(" ".join(list(map(str, arr))))
