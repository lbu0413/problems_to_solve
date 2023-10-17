C, N = map(int, input().split())

puppies = [int(input()) for _ in range(N)]


def dfs(idx, current, tmp):
    global total

    if current > C:
        return

    if current + (total - tmp) < total:
        return

    if idx == N:
        if current > total:
            total = current
    else:
        dfs(idx + 1, current + puppies[idx], tmp + puppies[idx])
        dfs(idx + 1, current, tmp + puppies[idx])


total = 0
dfs(0, 0, 0)
print(total)
