# boj1448

# 막대 3개로 삼각형을 만들기 위한 조건

import sys

N = int(sys.stdin.readline())
sides = [int(sys.stdin.readline()) for _ in range(N)]


answer = -1

sides.sort()

for i in range(len(sides) - 1, 1, -1):
    if sides[i] < sides[i - 1] + sides[i - 2]:
        answer = sides[i] + sides[i - 1] + sides[i - 2]
        break


print(answer)
