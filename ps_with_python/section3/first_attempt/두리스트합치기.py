N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

size = min(N, M)
ans = []
N_inc = 0
M_inc = 0

while N_inc < N and M_inc < M:
    if N_list[N_inc] < M_list[M_inc]:
        ans.append(N_list[N_inc])
        N_inc += 1

    elif N_list[N_inc] > M_list[M_inc]:
        ans.append(M_list[M_inc])
        M_inc += 1

    else:
        ans.append(N_list[N_inc])
        N_inc += 1

if N_inc < N:
    while N_inc < N:
        ans.append(N_list[N_inc])
        N_inc += 1

else:
    while M_inc < M:
        ans.append(M_list[M_inc])
        M_inc += 1

print(" ".join(map(str, ans)))
