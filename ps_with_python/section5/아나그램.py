str1 = input()
str2 = input()

dic1 = {}
dic2 = {}

if len(str1) != len(str2):
    print("NO")

for i in str1:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1

for j in str2:
    if j in dic2:
        dic2[j] += 1
    else:
        dic2[j] = 1

if dic1 == dic2:
    print("YES")
else:
    print("NO")
