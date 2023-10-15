from collections import deque

N, M = map(int, input().split())
urgent_level = list(map(int, input().split()))

Q = deque([(idx, i) for idx, i in enumerate(urgent_level)])
cnt = 0

while True:
    current = Q.popleft()
    if any(current[1] < x[1] for x in Q):
        Q.append(current)

    else:
        if current[0] == M:
            cnt += 1
            break
        else:
            cnt += 1

print(cnt)
