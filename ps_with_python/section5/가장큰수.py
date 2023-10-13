nums, K = map(int, input().split())
nums = list(map(int, str(nums)))

stack = []


for i in nums:
    while stack and K > 0 and stack[-1] < i:
        stack.pop()
        K -= 1

    stack.append(i)


while K > 0:
    stack.pop()
    K -= 1

print("".join(map(str, stack)))
