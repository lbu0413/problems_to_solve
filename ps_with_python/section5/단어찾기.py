n = int(input())


hash = {}
for i in range(n):
    word = input()
    hash[word] = 0

for i in range(n - 1):
    word = input()
    hash[word] += 1

for i in hash:
    if hash[i] == 0:
        print(i)
