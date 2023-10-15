input_str = list(input())

stack = []
ans_str = ""

for i in input_str:
    if i.isdigit():
        ans_str += i

    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            ans_str += stack.pop()
        stack.append(i)

    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ans_str += stack.pop()
        stack.append(i)

    elif i == ")":
        while stack and stack[-1] != "(":
            ans_str += stack.pop()
        stack.pop()

    elif i == "(":
        stack.append(i)

while stack:
    ans_str += stack.pop()

print(ans_str)
