import heapq as hq


hq_list = []

while True:
    num = int(input())

    if num == -1:
        break

    if num == 0:
        if len(hq_list) == 0:
            print(-1)
        else:
            print("ans", hq.heappop(hq_list))

    else:
        hq.heappush(hq_list, num)
