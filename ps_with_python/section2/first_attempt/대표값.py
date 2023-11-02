N = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / N)
minimum = 2147000000

for student_idx, student in enumerate(scores):
    tmp = abs(student - avg)
    if tmp < minimum:
        minimum = tmp
        answer_student = student
        answer_student_no = student_idx

    elif tmp == minimum:
        if scores[student_idx] > scores[answer_student_no]:
            answer_student = scores[student_idx]
            answer_student_no = student_idx

print(avg, answer_student_no + 1)
