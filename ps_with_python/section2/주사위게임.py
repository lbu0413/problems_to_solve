TC = int(input())


answer = 0
for i in range(TC):
    dice = list(map(int, input().split()))
    first = dice[0]
    second = dice[1]
    third = dice[2]
    if first == second and first == third:
        prize = 10000 + first * 1000

    elif first == second or first == third:
        prize = 1000 + first * 100

    elif second == third:
        prize = 1000 + second * 100

    else:
        prize = max(first, second, third) * 100

    answer = max(answer, prize)

print(answer)
