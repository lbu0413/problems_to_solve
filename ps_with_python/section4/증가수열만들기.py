from collections import deque

N = int(input())

nums = list(map(int, input().split()))
queue = deque(nums)

ans_arr = []
ans_str = ""
current = float("-inf")

while True:
    if queue[0] > current and queue[-1] < current:
        current = queue[0]
        ans_arr.append(queue.popleft())
        ans_str += "L"

    elif queue[-1] > current and queue[0] < current:
        current = queue[-1]
        ans_arr.append(queue.pop())
        ans_str += "R"

    elif queue[0] > current and queue[-1] > current:
        if queue[0] < queue[-1]:
            current = queue[0]
            ans_arr.append(queue.popleft())
            ans_str += "L"
        else:
            current = queue[-1]
            ans_arr.append(queue.pop())
            ans_str += "R"

    else:
        break

print(len(ans_arr))
print(ans_str)
