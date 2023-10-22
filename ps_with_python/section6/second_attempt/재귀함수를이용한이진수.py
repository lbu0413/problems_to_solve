N = int(input())


ans = ""


def dfs(num):
    global ans
    if num == 0:
        return
    dfs(num // 2)
    ans = ans + str(num % 2)


dfs(N)
print(ans)
