N, M = map(int, input().split())


counter = {}
answer = ""
for i in range(1, N + 1):
    for j in range(1, M + 1):
        add = i + j
        if add not in counter:
            counter[add] = 0
        counter[add] += 1


max_val = 0
answer = ""
for i in counter:
    if counter[i] > max_val:
        max_val = counter[i]
        answer = str(i)

    elif counter[i] == max_val:
        answer += " " + str(i)

print(answer)
