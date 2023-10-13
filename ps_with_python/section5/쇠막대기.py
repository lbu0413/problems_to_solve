pipes = list(input())


stack = []
cnt = 0

for i in range(len(pipes)):
    if pipes[i] == "(":
        stack.append(pipes[i])

    else:
        stack.pop()
        if pipes[i - 1] == "(":
            cnt += len(stack)

        else:
            cnt += 1
print(cnt)
