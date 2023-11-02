N = int(input())

nums = list(map(int, input().split()))

seq = [0] * N

for i in range(N):
    for j in range(N):
        if nums[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break

        elif seq[j] == 0:
            nums[i] -= 1


print(" ".join(map(str, seq)))
