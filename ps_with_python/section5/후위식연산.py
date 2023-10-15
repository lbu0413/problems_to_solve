input_str = list(input())

stack = []
ans = 0

for i in input_str:
    if i.isdigit():
        stack.append(i)

    else:
        if i == "+":
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(first + second)

        if i == "-":
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second - first)

        if i == "*":
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(first * second)

        if i == "/":
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second / first)

print(stack.pop())
