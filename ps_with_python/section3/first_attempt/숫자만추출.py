given_string = input()

answer = ""
for i in given_string:
    if i.isnumeric():
        answer += i


answer = int(answer)
cnt = 0

for i in range(1, answer + 1):
    if answer % i == 0:
        cnt += 1

print(answer)
print(cnt)
