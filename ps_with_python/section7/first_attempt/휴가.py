N = int(input())

time_a = []
pay_a = []
total = 0

for i in range(N):
    a, b = map(int, input().split())
    time_a.append(a)
    pay_a.append(b)

time_a.insert(0, 0)
pay_a.insert(0, 0)


def dfs(level, current_sum):
    global total

    if level == N + 1:
        if current_sum > total:
            total = current_sum

    else:
        if level + time_a[level] <= N + 1:
            dfs(level + time_a[level], current_sum + pay_a[level])
        dfs(level + 1, current_sum)


dfs(1, 0)
print(total)
