# https://www.acmicpc.net/problem/1816

n = int(input())
for _ in range(n):
    tc = int(input())

    for i in range(2, 1_000_001):
        if tc % i == 0:
            print("NO")
            break
        
        if i == 1_000_000:
            print("YES")