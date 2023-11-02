import heapq as hq

max_heap = []


while True:
    num = int(input())
    if num == -1:
        break

    if num == 0:
        if len(max_heap) == 0:
            print(-1)
        else:
            print("ans", hq.heappop(max_heap)[1])

    else:
        hq.heappush(max_heap, (-num, num))
