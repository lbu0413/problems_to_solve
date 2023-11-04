N, M = map(int, input().split())

MAX = 1000 * 1000 + 1

arr_a = [0] * MAX
arr_b = [0] * MAX


time_a = 1
for _ in range(N):
    v, t = map(int, input().split())

    for _ in range(t):
        arr_a[time_a] = arr_a[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(M):
    v, t = map(int, input().split())

    for _ in range(t):
        arr_b[time_b] = arr_b[time_b - 1] + v
        time_b += 1


leader, cnt = "", 0
for i in range(1, time_a):
    if arr_a[i] == arr_b[i] and leader != "A and B":
        leader = "A and B"
        cnt += 1

    elif arr_a[i] > arr_b[i] and leader != "A":
        leader = "A"
        cnt += 1

    elif arr_b[i] > arr_a[i] and leader != "B":
        leader = "B"
        cnt += 1


print(cnt)
