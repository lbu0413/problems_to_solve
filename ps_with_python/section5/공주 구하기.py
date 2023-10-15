from collections import deque

N, K = map(int, input().split())

rescues = deque([i for i in range(1, N + 1)])


while len(rescues) > 1:
    for i in range(K - 1):
        rescues.append(rescues.popleft())
    rescues.popleft()

print(rescues)
