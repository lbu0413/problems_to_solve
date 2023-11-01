N = int(input())
students = list(map(int, input().split()))

avg = sum(students) / N
avg = int(avg + 0.5)
min_ = float("inf")

min_num = 0
min_idx = 0


for idx, student in enumerate(students):
    tmp = abs(avg - student)

    if tmp < min_:
        min_ = tmp
        min_num = student
        min_idx = idx

    elif tmp == min_:
        if student > min_num:
            min_num = student
            min_idx = idx


print(avg, min_idx + 1)
