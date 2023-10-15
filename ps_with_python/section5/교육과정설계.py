from collections import deque


input_str = list(input())

N = int(input())


for i in range(N):
    classes = list(input())
    Q = deque(input_str)
    for x in classes:
        if len(Q) == 0:
            print(f"#{i+1} YES")
            break
        if x == Q[0]:
            Q.popleft()
        else:
            if x in Q:
                print(f"#{i+1} NO")
                break
    else:
        if len(Q) != 0:
            print(f"#{i+1} NO")
        else:
            print(f"#{i+1} YES")
