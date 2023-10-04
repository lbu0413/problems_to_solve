# https://chancoding.tistory.com/45
n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

hashmap = {}

for i in n_nums:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(" ".join(str(hashmap[j])) if j in hashmap else "0" for j in m_nums)
