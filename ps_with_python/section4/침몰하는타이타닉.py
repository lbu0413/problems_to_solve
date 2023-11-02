from collections import deque

N, M = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()

boat_count = 0


queue = deque(weights)


while len(queue) != 0:
    if len(queue) == 1:
        boat_count += 1
        break

    if queue[0] + queue[-1] > M:
        queue.pop()
        boat_count += 1

    else:
        queue.pop()
        queue.popleft()
        boat_count += 1


print(boat_count)
