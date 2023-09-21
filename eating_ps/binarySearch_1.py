# #boj2512

number_of_districts = int(input())
requests = list(map(int, input().split()))
budget = int(input())


def calculate_needed_budget(upper_bound):
    needed_budget = 0

    for request in requests:
        needed_budget += min(request, upper_bound)
    
    return needed_budget


low = 0
high = max(requests)

while low <= high:
    mid = (low + high) // 2

    if calculate_needed_budget(mid) <= budget:
        good_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1


answer = -1
for request in requests:
    given = min(request, good_upper_bound)
    answer = max(given, answer)


print(answer)