import sys

N = int(input())

for i in range(N):
    input_ = input().lower()
    ln = len(input_)
    mid = ln // 2

    for j in range(mid):
        if input_[j] != input_[ln - 1 - j]:
            ans = "NO"
            break
    else:
        ans = "YES"

    print(f"#{i+1} {ans}")
